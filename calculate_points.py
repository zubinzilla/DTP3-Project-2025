from GUI import *
from file_reading import file_read_status

calculate_points_status = 0


# checks if no errors occured in previous modules
if file_read_status == 0 and GUI_status == 0:
    from file_reading import final_results
    from GUI import maximum_points

    if maximum_points is None:
        maximum_points = 13

    regional_totals = {}

    # default score for all teams set to 0
    for placing, regional_association in final_results:
        regional_totals[regional_association] = 0

    for placing, regional_association in final_results:
        # deduction system, lower placing gets lower amount of points
        points = maximum_points - (int(placing) - 1)
        if points > 0:
            regional_totals[regional_association] += points
        # cutoff for points if only a certain bracket of racers are awarded points (maximum points < number of placings)
        else:
            continue

    # sorts regional associations by points, descending order
    sorted_totals = list(sorted(regional_totals.items(), key=lambda result: result[1], reverse=True))



    # adding place equivalents for points

    final_sorted_results = []
    current_place = 0
    prev_points = None
    num_tied = 0  # count how many tied at previous place

    for index, (name, points) in enumerate(sorted_totals):

        # excludes any blank records
        if len(name) > 0:
            if points == prev_points:
                # same points as previous → place stays the same
                num_tied += 1
            else:
                # new points → increment place by number of tied teams previously
                current_place = current_place + num_tied + 1
                num_tied = 0  # reset tie count for new points
            final_sorted_results.append((current_place, name, points))
            prev_points = points

    # Print results
    for place, name, points in final_sorted_results:
        print(f"{place}. {name} - {points} pts")


else:
    calculate_points_status = 1















