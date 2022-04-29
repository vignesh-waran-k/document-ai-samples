# type: ignore[1]
"""
Cloud Storage Utility Functions
"""
import re

from typing import List, Tuple, Any

from google.protobuf.json_format import ParseError

from google.cloud import documentai_v1 as documentai
from google.cloud import storage

from consts import (
    GCS_INPUT_BUCKET,
    GCS_INPUT_PREFIX,
    GCS_OUTPUT_BUCKET,
    GCS_OUTPUT_PREFIX,
    GCS_ARCHIVE_BUCKET,
    BATCH_MAX_FILES,
    ACCEPTED_MIME_TYPES,
)

storage_client = storage.Client()


def split_gcs_uri(gcs_uri: str) -> Tuple[str, str]:
    """
    Split GCS URI into bucket and file path
    """

    return re.match("gs://(.*?)/(.*)", gcs_uri).groups()


def get_blob_from_gcs(bucket_name: str, object_name: str) -> storage.Blob:
    """
    Get File from GCS as bytes
    """

    return storage_client.bucket(bucket_name).blob(object_name)


def upload_file_to_gcs(file_obj: Any, bucket_name: str, object_name: str) -> None:
    """
    Upload file to GCS
    """

    storage_client.bucket(bucket_name).blob(object_name).upload_from_file(file_obj)


def create_batches(
    input_bucket: str = GCS_INPUT_BUCKET,
    input_prefix: str = GCS_INPUT_PREFIX,
    batch_size: int = BATCH_MAX_FILES,
) -> List[List[documentai.GcsDocument]]:
    """
    Create batches of documents to process
    """
    if batch_size > BATCH_MAX_FILES:
        raise ValueError(
            f"Batch size must be less than {BATCH_MAX_FILES}. "
            f"You provided {batch_size}"
        )

    blob_list = storage_client.list_blobs(input_bucket, prefix=input_prefix)

    batches: List[List[documentai.GcsDocument]] = []
    batch: List[documentai.GcsDocument] = []

    for blob in blob_list:

        if blob.content_type not in ACCEPTED_MIME_TYPES:
            print(f"Invalid Mime Type {blob.content_type} - Skipping file {blob.name}")
            continue

        if len(batch) == batch_size:
            batches.append(batch)
            batch = []

        batch.append(
            documentai.GcsDocument(
                gcs_uri=f"gs://{input_bucket}/{blob.name}",
                mime_type=blob.content_type,
            )
        )

    batches.append(batch)

    return batches


def get_document_protos_from_gcs(
    operation_id: str,
    gcs_bucket: str = GCS_OUTPUT_BUCKET,
    gcs_prefix: str = GCS_OUTPUT_PREFIX,
) -> List[documentai.Document]:
    """
    Download document proto output from GCS.
    """

    # Output files will be in a new subdirectory with Operation ID as the name

    op_re = re.search(r"operations\/(\d+)", operation_id, re.IGNORECASE)

    if op_re is None or op_re.group(1) is None:
        raise ValueError(f"Invalid Operation ID: {operation_id}")

    operation_number = op_re.group(1)
    output_directory = f"{gcs_prefix}/{operation_number}"

    # List of all of the files in the directory
    # `gs://gcs_bucket/gcs_prefix/operation_id`
    blob_list = storage_client.list_blobs(gcs_bucket, prefix=output_directory)

    output_documents = []

    for blob in blob_list:
        print("Fetching from " + blob.name)

        # Document AI should only output JSON files to GCS
        if ".json" in blob.name:
            try:
                output_document = documentai.types.Document.from_json(
                    blob.download_as_bytes(), ignore_unknown_fields=True
                )
                output_documents.append(output_document)
            except ParseError:
                print(f"Failed to parse {blob.name}")
                continue
        else:
            print(f"Skipping non-supported file type {blob.name}")

    return output_documents


def cleanup_gcs(
    input_bucket: str = GCS_INPUT_BUCKET,
    input_prefix: str = GCS_INPUT_PREFIX,
    archive_bucket: str = GCS_ARCHIVE_BUCKET,
):
    """
    Moving Input Files to Archive
    """

    delete_queue = []

    # Copy input files to archive bucket
    source_bucket = storage_client.bucket(input_bucket)
    destination_bucket = storage_client.bucket(archive_bucket)

    source_blobs = storage_client.list_blobs(input_bucket, prefix=input_prefix)

    for source_blob in source_blobs:
        print(
            f"Moving {source_bucket}/{source_blob.name} to {archive_bucket}/{source_blob.name}"
        )
        source_bucket.copy_blob(source_blob, destination_bucket, source_blob.name)
        delete_queue.append(source_blob)

    for blob in delete_queue:
        print(f"Deleting {blob.name}")
        blob.delete()
