from customtkinter import *
import tkinter as tk

# final value sent to 'file_reading.py' to be analyzed
target_year = 0

def check_input():
    global target_year
    try:
        input_year = int(entry_label.get())
        # boundary test
        if 2017 <= input_year <= 2040:
            response_variable.set("Valid year")
            target_year = input_year
        else:
            response_variable.set("Entered year not between 2017 and 2040!")

    # user input not a year (an integer)
    except ValueError:
        response_variable.set("You did not enter a year!")
app = CTk()
app.geometry('500x500')

response_variable = tk.StringVar()

set_appearance_mode("dark")
set_default_color_theme("green")

main_label = CTkLabel(master=app, text="Analyse a Waka Ama National Game by year.", height=20, width=100, anchor="center", font=("Arial", 16))
main_label.place(relx=0.2, rely=0.4)

# Display system response to user input
response_label = CTkLabel(master=app, textvariable=response_variable, height=20, width=255, font=("Arial", 20), bg_color="#545454"
                          ,anchor="center")
response_label.place(relx=0.255, rely=0.27)

entry_label = CTkEntry (master=app, placeholder_text="Enter a year between 2017-2040", width=200)
entry_label.place(relx=0.3, rely=0.5)

submit_button = CTkButton(master=app, width=200, text="Submit", command=check_input)
submit_button.place(relx=0.3, rely=0.57)

app.mainloop()

