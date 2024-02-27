# Purpose and Description

This tool uses parsed json files and a list of entities in which date format has to be changed( if empty all the date entities are changed).The normalized value in currency entity which is predicted as USD sometimes changed to SGD and normalized date format to the format needed as per the input.

# Input Details

* **project_id** : Enter your GCP project ID
* **entities_normalize** : list of entities to be changed for date , if its empty all the date related entities will be updated 
Below are the changes made for the entities given in the list entitites_normalize list
        1. Default google normalized value of currency from USD to SGD
        2. Default google normalized date format will be changed to the format given in the normalized_date_format (The date format changes only 
    in the JSON but changes doesnt reflect in UI)
    
* **input_files_path**: GCS folder URI where parsed json files are stored
* **output_files_path**: GCS Folder URI where the updated Jsons have to be stored
* **normalized_date_format**: Specific Date format to replace the default normalized date format day/month/year
* **switch**: Either `ON` or `OFF` to update the jsons.
    * **ON**: Renaming normalize current processing takes place
    * **OFF**: JSON files copied from *INPUT_FILES_PATH* to *OUTPUT_FILES_PATH*(i.e, with-out postprocessing)
    
# Output Details

* Changes the normalized value from USD to SGD as shown below and saves the updated jsons in the output GCS folder.

<img src="./images/pre_process.png" width=400 height=800>

* Updates the date format as needed and given in the input details(i.e, based on format provided `normalized_date_format` variable)

<table>
<tr>
<td> Pre-processing</td>
<td> Post-processing</td>
</tr>
<tr>
<td><img src="./images/pre_process.png" width=400 height=800></td>
<td><img src="./images/post_process.png" width=400 height=800></td>
</tr>
</table>

**NOTE**: But this date change should not be visible in the UI.

Output of above testing script is a csv of comparison file wise on currency entity as below

<img src="./images/test_result.png" width=400 height=800>