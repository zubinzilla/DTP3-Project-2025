import os

from GUI import maximum_points, GUI_status
file_read_status = None

print(maximum_points, type(maximum_points))


def award_points(sorted_recs, max_points):
    results_with_points = []
    #for i, (regional_association, elapsed_time) in enumerate(sort_recs):
    for i, rec in enumerate(sorted_recs):
        regional_association, elapsed_time = rec
        if elapsed_time == float('inf'):
            results_with_points.append([0, regional_association])
        else:
            points = max_points - i
            if points > 0:
                results_with_points.append([points, regional_association])
            else:
                results_with_points.append([1, regional_association])
    return results_with_points

def convert_time(t):
    # rest > rest of the seconds
    if t != '':
        time_list = t.split(':')
        minutes = int(time_list[0]) * 60
        seconds = float(time_list[1])
        return float(minutes) + seconds
    else:
        return float('inf')


# no error occured
if GUI_status == 0:
    # no valid target year found (0 as default value)
    from GUI import target_year

    folder_path = "C:/Users/Lenovo/Downloads/dtpAssignmentResources/3.7B resource files/3.7B resource files/WakaNats" + str(
        target_year)

    # if folder path exists
    if os.path.isdir(folder_path):

        final_filepaths = []
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

            # filepath > heat
            with open(filepath, "r") as file:
                content = file.read() # would represent string data
                heat_records = content.split('\n')
                # splits content into array of records
                heat_records.pop(0)

                updated_list = []

                for record in heat_records:
                    results = record.split(',')
                    if len(record) != 0:
                        updated_list.append([results[5], convert_time(results[6])])


                    # sort by elapsed time
                sorted_results = sorted(updated_list, key=lambda x: x[1])
                # awards points and adds to the array with all records
                all_records.append(award_points(sorted_results, maximum_points))

        file_read_status = 0
    else:
        file_read_status = 1



