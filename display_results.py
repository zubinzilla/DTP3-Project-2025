import tkinter
from customtkinter import *
from GUI import target_year
from calculate_points import calculate_points_status, file_read_status, GUI_status


results_window = CTk()
results_window.geometry('500x400')

if calculate_points_status == 0:
    # initialize results display

    from calculate_points import final_sorted_results

    # final sorted results actually has data in it
    if len(final_sorted_results) != 0:

        results_window.title(f"Regional Association Results from {target_year} Waka Ama Games.")
        results_window.geometry("500x400")


        # allows user to scroll through results
        scrollable_frame = CTkScrollableFrame(results_window)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # headings for place, regional association and points
        for col, heading in enumerate(["Place", "Regional Association", "Points"]):
            label = CTkLabel(scrollable_frame, text=heading, font=("Arial", 16, "bold"))
            label.grid(row=0, column=col, padx=20, pady=10, sticky="w")

        # Display results in a spreadsheet like manner
        for row, (place, name, points) in enumerate(final_sorted_results, start=1):
            CTkLabel(scrollable_frame, text=str(place), font=("Arial", 14)).grid(row=row, column=0, padx=20, pady=5,
                                                                                     sticky="w")
            CTkLabel(scrollable_frame, text=name, font=("Arial", 14)).grid(row=row, column=1, padx=20, pady=5,
                                                                               sticky="w")
            CTkLabel(scrollable_frame, text=str(points), font=("Arial", 14)).grid(row=row, column=2, padx=20,
                                                                                      pady=5, sticky="w")

else:
    results_window.geometry('800x400')
    results_window.title("Error window.")
    error_list = []

    if file_read_status != 0:
        error_list.append(
            "File Reading Error: The folderpath for the Waka Ama game selected does not exist on the system.")
    if GUI_status != 0:
        error_list.append(
            "GUI Error: Year value and max points value were invalid or was not entered before analyzing.")

    temp_string = ""

    for error in error_list:
        temp_string += f" {error}\n"

    # display possible errors
    error_text = tkinter.StringVar()
    error_text.set(temp_string)

    error_label = CTkLabel(master=results_window, textvariable=error_text, font=("Arial", 15, "bold"))
    error_label.place(x=60, y=100)

results_window.mainloop()