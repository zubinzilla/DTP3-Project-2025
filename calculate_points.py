
from file_reading import file_read_status
from GUI import GUI_status

# function for totalling points to each regional association

calculate_points_status = None

# function for totalling points
def total_points(all_results):
    # dict > regional association and points, key value pair
    regional_association_totals = {}

    for heat in all_results:
        for points, regional_association in heat:
            if regional_association in regional_association_totals:
                # sums points to regional association
                regional_association_totals[regional_association] += points
            else:
                regional_association_totals[regional_association] = points

    # sorts points by ascending order
    regional_association_totals = sorted(regional_association_totals.items(), key=lambda result: result[1], reverse=True)
    return regional_association_totals

if file_read_status == 0:
    from file_reading import all_records
    all_records = total_points(all_records)
    print(all_records)
    calculate_points_status = 0

else:
    print("Error")
    calculate_points_status = 1



















