import os

folder_path = "C:/Users/jaden/Downloads/DTP3 Project/3.7B resource files/3.7B resource files/WakaNats2017"
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
        for record in file_records:
            final_results.append(record.split(","))

print(f"Folder Opened: ")
print(f"'{folder_path}'")
print("Number of files: ")
print(f"{no_of_files} files found.")

print("Records: ")
for record in final_results:
    print(record)
