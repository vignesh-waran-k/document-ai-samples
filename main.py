"""
Reference architecture asynchronous main.py
"""

import concurrent.futures
from typing import List
import pandas as pd
from google.cloud import documentai, firestore, storage
from utilities import batch_process_documents_sample, copy_blob, list_blobs

INPUT_BUCKET_NAME = "your_test_bucket_name"
GCS_OUTPUT_URI_PREFIX = "your_output_folder_prefix"

# read the config data
storage_client = storage.Client()
bucket = storage_client.bucket(INPUT_BUCKET_NAME)
blob = bucket.blob("config/config.txt") 
config_data = blob.download_as_string().decode("utf-8")

print(str(config_data).split("\n"))

input_parameters = str(config_data).split("\n")
project_name = input_parameters[0].split(":")[1].strip()
location = input_parameters[2].split(":")[1].strip()
processor_id = input_parameters[6].split("/")[-1]
project_id = input_parameters[6].split("/")[1]

print("INPUT_BUCKET_NAME", INPUT_BUCKET_NAME)
print("project_name ", project_name)
print("location ", location)
print("processor_id ", processor_id)
print("project_id ", project_id)

metadata_array = []

connection = firestore.Client(project=project_name)


def delete_blob(bucket_name: str, blob_name: str) -> None:
    """
    Deletes specified blob name from Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket.
        blob_name (str): The name of the blob inside the bucket.

    Returns:
        None. If the blob exists, it will be deleted. If it doesn't exist or an error occurs,
        the function will log the error. This example catches ValueError and TypeError as
        placeholders for more specific exceptions you might want to handle.
    """
    print("delete_blob")
    storage_client_db = storage.Client()
    bucket_db = storage_client_db.bucket(bucket_name)
    blob_db = bucket_db.blob(blob_name)
    try:
        # Example operation that could, in theory, raise a ValueError or TypeError
        if not isinstance(bucket_name, str) or not isinstance(blob_name, str):
            raise ValueError("Bucket name and blob name must be strings.")
        if bucket_name is None or blob_name is None:
            raise TypeError("Bucket name and blob name cannot be None.")

        blob_db.delete()
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
    except TypeError as te:
        print(f"TypeError occurred: {te}")


def bucket_cleaner(bucket_name: str) -> None:
    """
    Deletes all the blob inside the Google Cloud Storage bucket .

    Args:
        bucket_name (str): The name of the bucket from where the blobs need to be deleted.
    """
    print("bucket_cleaner")
    bucket_blobs_list = list_blobs(bucket_name)
    for i in bucket_blobs_list:
        delete_blob(bucket_name, i)


def db_insert(info_list_holder: List) -> None:
    """
    Function to write the logs in the database having file_name as the primary key.

    Args:
        info_list_holder (List): The list of all the details related to the documents which
        contains metadata of the file, operation id, file storage location.
    """
    print("db_insert")
    for i in info_list_holder:
        for j in i:
            file_name = j["filename"]
            doc_reference = connection.collection("daira_logs").document(file_name)
            doc_reference.set(j)


def db_print() -> pd.DataFrame:
    """
    Function to get all the logs stored in database name 'daira_logs' and store it in a dataframe.

    Return (pd.DataFrame):

            It returns the dataframe having all the logs from the database.
    """
    print("db_print")
    db_entries = []
    reference = connection.collection("daira_logs")
    docs = reference.stream()
    for doc in docs:
        db_entries.append(doc.to_dict())
    db_dataframe = pd.DataFrame(db_entries)
    return db_dataframe


def bucket_lister(bucket_name: str) -> List:
    """
    Collects all the file name and create the GCS bucket path of the file in the given bucket name.

    Args:
        bucket_name (str): The name of the bucket from where the blobs need to be discovered.

    Returns (List):
        The list having the full GCS path of thr file inside the bucket name provided by the user.
    """

    print("bucket_lister")
    storage_client_bl = storage.Client()
    blobs = storage_client_bl.list_blobs(bucket_name)
    blob_arr = []
    for blob_bl in blobs:
        blob_arr.append("gs://" + bucket_name + "/" + blob_bl.name)
    return blob_arr


def create_bucket_class_location(bucket_name: str) -> str:
    """
    It will create a specified Google Cloud Storage bucket with the US region .

    Args:
        bucket_name (str): The name of the bucket to create.

    Returns:
        str:
        The bucket name as string form.
    """
    print("create_bucket_class_location")
    storage_client_cb = storage.Client()
    bucket_cb = storage_client_cb.bucket(bucket_name)
    print("Bucket Created successfully : ", bucket_cb)
    return bucket_cb


def batch_caller(gcs_input_uri, gcs_output_uri):
    """It will perform Batch Process by calling the batch_process_documents_sample function.

    Args:
        gcs_input_uri (str): GCS path which contains all input files
        gcs_output_uri (str): GCS path to store processed JSON results
    """
    print(gcs_input_uri, gcs_output_uri)
    print("BATCH_CALLER project_id : ", project_id)
    operation = batch_process_documents_sample(
        project_id,
        location,
        processor_id,
        gcs_input_uri,
        f"{gcs_output_uri}/{GCS_OUTPUT_URI_PREFIX}/",
    )
    metadata = documentai.BatchProcessMetadata(operation.metadata)
    metadata_array.append(metadata)


def metadata_reader(metadata: documentai.BatchProcessMetadata) -> List:
    """It will read the metadata details from the batch processsed and store it in an array.

    Args:
        metadata (str): GCS path which contains all input files

    Return:
        List:
        Returns list with all the required metadata of the files.
    """
    print("metadata_reader")
    info_array = []
    metadata_ips = metadata.individual_process_statuses
    metadata_state = metadata.state.name
    metadata_createtime = metadata.create_time.ctime()
    metadata_updatetime = metadata.update_time.ctime()
    for i in metadata_ips:
        info_array.append(
            {
                "filename": i.input_gcs_source.split("/")[-1],
                "metadata_state": metadata_state,
                "metadata_createtime": metadata_createtime,
                "metadata_updatetime": metadata_updatetime,
                "operation_id": i.output_gcs_destination.split("/")[-2],
                "file_output_gcs_destination": i.output_gcs_destination,
                "file_human_review_status": i.human_review_status.state.name,
                "file_human_review_operation_id":
                i.human_review_status.human_review_operation.split("/")[-1],
            }
        )
    return info_array


def file_copy(array_having_file_names: List, bucket_name_with_folder: str) -> None:
    """
    Copies a blob (file/object) from one GCP storage bucket to another.

    Args:
        array_having_file_names (List) : List of file names
        blob_name (str): Name of the blob (file/object) in the source bucket to be copied.
        destination_bucket_name (str): Name of the destination bucket.
        destination_blob_name (str): Desired name for the blob in the destination bucket.

    Output:
        None. The blob is copied to the destination bucket with the specified name.
    """
    print("file_copy")
    for i in array_having_file_names:
        bucket_name = i.split("/")[-2]
        blob_name = i.split("/")[-1]
        destination_bucket_name = bucket_name_with_folder.split("/")[2]
        temp = bucket_name_with_folder.split("/")[3:]
        destination_blob_name = "/".join(temp) + blob_name
        print(
            "-- copy_blob --> ",
            bucket_name,
            "|",
            blob_name,
            "|",
            destination_bucket_name,
            "|",
            destination_blob_name,
        )
        copy_blob(
            bucket_name, blob_name, destination_bucket_name, destination_blob_name
        )


def concurrent_processing(
    daira_output_test: str, batch_array: List
) -> None:
    """
    To create a concurrent process for batch processing the files .

    Args:
        batch_caller (Function) : Function which will call the batch processing
        daira_output_test (str): A temporary bucket name where all
        the batch processed file get stored.
        batch_array (List): List of all the copied files from
        temporary bucket which needs to processed.
    """
    print("--concurrent_processing--")
    print(daira_output_test, batch_array)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        print("processing completed", executor)

def hello_world() -> str:
    """
    HTTP Cloud Function which will get deployed and run by the cloud scheduler every hour.
    For more information on how to deploy cloud function
    https://cloud.google.com/functions/docs/create-deploy-gcloud-1st-gen.
    
    Return:
        str:
        Returns the success message.

    """
    print("--STARTED--")

    # delete previous ran diara-logs in firestore - if u r testing for same
    # files
    try:
        previously_done_files = list(db_print()["filename"])
        print("previously_done_files : ", previously_done_files)
    except KeyError as ke:
        # This catches cases where the 'filename' key is missing.
        print(f"KeyError - The 'filename' key was not found: {ke}")
        previously_done_files = []
    except TypeError as te:
        # This catches cases where the result of db_print() is not a dictionary or is None.
        print(f"TypeError - There was a type issue with the db_print() response: {te}")
        previously_done_files = []

    input_bucket_files_list = bucket_lister(INPUT_BUCKET_NAME)

    # pop the element (config file) from the input bucket file
    input_bucket_files_list.remove("gs://" + INPUT_BUCKET_NAME + "/config/config.txt")

    files_to_process = [
        i
        for i in input_bucket_files_list
        if i.split("/")[-1] not in previously_done_files
    ]
    print("files_to_process : ", files_to_process)
    start = 0
    end = len(files_to_process)
    step = 50

    process_batch_array = []
    for i in range(start, end, step):
        x = i
        process_batch_array.append(files_to_process[x : x + step])
    print("process_batch_array : ", process_batch_array)

    # test vars
    diara_processing_test = "daira-processing-test02"
    daira_output_test = "daira-output-test02"

    try:
        print("creating : daira-processing-test")
        create_bucket_class_location(diara_processing_test)  # 'daira-processing-test03'
        print("creating : daira-output-test")
        create_bucket_class_location(daira_output_test)  # 'daira-output-test03'
    except KeyError as ke:
        print(f"An error occurred during bucket creation.{ke}")

    bucket_cleaner(diara_processing_test)  # 'daira-processing-test03'
    lenght = len(process_batch_array)
    print(process_batch_array)

    for i, array_having_file_names in enumerate(process_batch_array):
        bucket_name_with_folder = "gs://" + diara_processing_test + "/batches/" + str(i) + "/"
        print(i, " | ", array_having_file_names, " | ", bucket_name_with_folder)
        file_copy(array_having_file_names, bucket_name_with_folder)

    batch_array = [
        "gs://" + diara_processing_test + "/batches/" + str(i) + "/"
        for i in range(lenght)
    ]
    print(batch_array)

    concurrent_processing(daira_output_test, batch_array)

    print("metadata_array:")
    print(metadata_array)

    info_list_holder = [metadata_reader(i) for i in metadata_array]
    db_insert(info_list_holder)
    print(info_list_holder)
    print("--ENDED--")
    return "Diara Done!"
