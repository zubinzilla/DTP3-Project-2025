if __name__ == "__main__":

    import csv
    import tkinter
    from customtkinter import *

    from GUI import target_year, GUI_status
    from calculate_points import calculate_points_status
    from file_reading import file_read_status

    # save results as a csv file
    def save_results():
        # file dialog, allows the user to save csv file where they want to
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        # after user selects a filepath
        if file_path:

            # write data into csv file
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Regional Association", "Points"])  # Header
                for association, no_of_points in all_records:
                    writer.writerow([association, no_of_points])

    results_window = CTk()
    results_window.geometry('700x400')

    if calculate_points_status == 0:
        # initialize results display

        from calculate_points import all_records

        # final sorted results actually has data in it
        if len(all_records) != 0:

            results_window.title(f"FULL CLUB POINTS FROM {target_year} WAKA AMA GAMES.")
            results_window.geometry("500x700")


            # allows user to scroll through results
            scrollable_frame = CTkScrollableFrame(results_window)
            scrollable_frame.pack(fill="both", expand=True, padx=20, pady=40)

            # headings for place, regional association and points
            for col, heading in enumerate(["Regional Association", "Points"]):
                label = CTkLabel(scrollable_frame, text=heading, font=("Arial", 16, "bold"))
                label.grid(row=0, column=col, padx=20, pady=10, sticky="w")

            # Display results in a spreadsheet like manner
            for row, (regional_association, points) in enumerate(all_records, start=1):
                CTkLabel(scrollable_frame, text=regional_association, font=("Arial", 14)).grid(row=row, column=0, padx=20, pady=5,
                                                                                         sticky="w")
                CTkLabel(scrollable_frame, text=str(points), font=("Arial", 14)).grid(row=row, column=1, padx=20, pady=5,
                                                                                   sticky="w")

            save_button = CTkButton(master=results_window, text="Save as .csv File", command=save_results)
            save_button.pack(pady=30)


    else:
        results_window.geometry('1000x400')
        results_window.title("Error window.")
        error_list = []


        # sends only one error (tracebacks to earliest source of error)
        while len(error_list) < 1:
            if GUI_status != 0:
                error_list.append(
                    "GUI Error: Year value and max points value were invalid or was not entered before analyzing.")
            elif file_read_status != 0:
                error_list.append(
                    "File Reading Error: The folder you selected does not contain the WakaNats folder you are searching for.")
            elif calculate_points_status != 0:
                error_list.append("Calculating points Error: There was an error during calculating points.")

        temp_string = ""

        for error in error_list:
            temp_string += f" {error}\n"

        # display possible errors
        error_text = tkinter.StringVar()
        error_text.set(temp_string)

        error_label = CTkLabel(master=results_window, textvariable=error_text, font=("Arial", 15, "bold"))
        error_label.pack(anchor="s")

    results_window.mainloop()