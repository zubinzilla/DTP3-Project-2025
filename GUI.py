from tkinter.filedialog import askdirectory

from customtkinter import *
import tkinter as tk


# allow the user to select the folder that WakaNats is in

# final value sent to 'file_reading.py' to be analyzed
target_year = None
maximum_points = None
directory = None

GUI_status = 0

analy_x = 100
max_x = 600
y_increment = 70

def fetch_folder():
    global directory
    directory = askdirectory()

# fetches maximum points for a year's race
def max_score():
    global maximum_points
    global GUI_status

    points_input = points_entry.get()
    if not points_input:
        GUI_status = 1
    else:
        try:
            points_input = int(points_input)
            if points_input > 0:
                points_response_variable.set("Valid maximum points.")
                maximum_points = points_input

            # user enters an integer smaller than 1
            else:
                points_response_variable.set("You did not enter an integer (> 0) for maximum points!")

        # user does not enter an integer
        except ValueError:
            points_response_variable.set("You did not enter an integer (> 0) for maximum points!")

# checks if user enters a year
def check_input():
    global target_year
    global GUI_status

    try:
        input_year = int(entry_label.get())
        # boundary test
        if 2017 <= input_year <= 2040:
            response_variable.set("Valid year")
            target_year = input_year
        else:
            GUI_status = 1
            response_variable.set("Entered year not between 2017 and 2040!")

    # user input not a year (an integer)
    except ValueError:
        response_variable.set("You did not enter a year!")
        GUI_status = 1

# checks if maximum points AND year is entered correctly
def valid_inputs():
    global GUI_status
    # checks if both points and target year are entered correctly
    global maximum_points
    global target_year
    if target_year is not None and maximum_points is not None:
        GUI_status = 0
    else:
        GUI_status = 1
    app.destroy()



app = CTk()
app.geometry('1000x1000')

points_response_variable = tk.StringVar()
response_variable = tk.StringVar()

set_appearance_mode("dark")
set_default_color_theme("green")

main_title = CTkLabel(master=app, text="Welcome to Waka Ama Game Analysis Application.", font=("Arial", 30))
main_title.place(x=160, y=20)

main_label = CTkLabel(master=app, text="Analyse a Waka Ama National Game by year.", height=20, width=100, anchor="center", font=("Arial", 16))


# Display system response to user input
response_label = CTkLabel(master=app, textvariable=response_variable, height=20, width=255, font=("Arial", 12), bg_color="#545454"
                          ,anchor="center")

entry_label = CTkEntry (master=app, placeholder_text="Enter a year between 2017-2040", width=200)

submit_button = CTkButton(master=app, width=200, text="Enter", command=check_input)

# widgets for points
points_label = CTkLabel(master=app, width=200, height=20,text="Enter maximum amount of points (integer) a team can get.", anchor="center", font=("Arial", 16))
points_entry = CTkEntry(master=app, width=200, placeholder_text="Maximum amount of points")
points_button = CTkButton(master=app, width=200, text="Enter", command=max_score)
points_response_label = CTkLabel(master=app, textvariable=points_response_variable, height=20, width=255, font=("Arial", 12), bg_color="#545454"
                          ,anchor="center")

analyze_button = CTkButton(master=app, text="Analyse year", width=200, command=valid_inputs)


analyze_info = CTkLabel(master=app, text="NOTE: You must enter BOTH the maximum number of points (points 1st place gets PER RACE)\n AND the year you want to analyze BEFORE you press the analyze button. To enter, ensure you press both enter buttons\n Otherwise, error will occur.", font=("Arial", 14), text_color="#fc0303")

select_folder_button = CTkButton(master=app, text="Select the folder all WakaNats folders are stored in.", command=fetch_folder)


# places all widgets on screen
main_label.place(x=analy_x-40, y=280)
response_label.place(x=analy_x-25, y=320)
entry_label.place(x=analy_x, y=360)
submit_button.place(x=analy_x, y=400)

points_label.place(x=max_x-60, y=280)
points_response_label.place(x=max_x-30, y=320)
points_entry.place(x=max_x, y=360)
points_button.place(x=max_x, y=400)

analyze_button.place(x=350, y=500)
analyze_info.place(x=70, y=540)

select_folder_button.place(x=300, y=100)





app.mainloop()

