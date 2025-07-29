import os
from check_filepath import target_year


# no valid target year found (0 as default value)
if target_year == 0:
    print("No valid year.")

# valid target year found
else:
    folder_path = "C:/Users/Lenovo/Downloads/dtpAssignmentResources/3.7B resource files/3.7B resource files/WakaNats" + str(
        target_year)

    # checks if folderpath exists
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

        print(f"Folder Opened: ")
        print(f"'{folder_path}'")
        print("Number of files: ")
        print(f"{no_of_files} files found.")

        print("Records: ")
        for record in final_results:
            print(record)
    else:
        print("No corresponding folder exists for that year.")