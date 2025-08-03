import os
from GUI import GUI_status

file_read_status = 0

# no error occured
if GUI_status == 0:
    # no valid target year found (0 as default value)
    from GUI import target_year

    folder_path = "C:/Users/Lenovo/Downloads/dtpAssignmentResources/3.7B resource files/3.7B resource files/WakaNats" + str(
        target_year)

    # if folder path exists
    if os.path.isdir(folder_path):

        final_filepaths = []
        final_results = []
        no_of_files = 0
        all_records = []

        # collects all the file names with the
        with os.scandir(folder_path) as folder:
            for file in folder:
                no_of_files += 1 # increments number of files for each file scanned in directory
                if "Final" in file.name:
                    final_filepaths.append(file.path)

        # processes the data of each file
        for filepath in final_filepaths:
            with open(filepath, "r") as file:
                content = file.read() # would represent string data
                file_records = content.split('\n') # splits content into array of records
                file_records.pop(0)
                for record in file_records:
                    if len(record) == 0:
                        file_records.pop(file_records.index(record))
                    else:
                        final_results.append(record.split(","))

        # strips records to only contain regional association and placing
        for record in final_results:
            updated_record = [record[2], record[5]]
            record[:] = updated_record
            del updated_record


        file_read_status = 0
    else:
        file_read_status = 1

