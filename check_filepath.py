from customtkinter import *
import re

# allow user to select directory from File Explorer
def openDir():
    filepath = filedialog.askdirectory()
    print(filepath)
    subdirectories = os.path.split(filepath)
    latest_sd = subdirectories[-1]

    folder_format = r"WakaNats\d{4}$"

    # compares subdirectory to WakaNats conventional folder naming.
    if re.fullmatch(folder_format, latest_sd):
        print("This is the correct format")
        folder_date = int(latest_sd[-4:])
        if (folder_date >= 2017) and (folder_date <= 2040):
            print("Folder date within valid date range (2017-2040).")
        else:
            print(f"Folder date {folder_date} not within valid date range (2017-2040).")
    else:
        print("This is not the correct format.")

app = CTk()
app.geometry('500x500')

set_appearance_mode("dark")
set_default_color_theme("green")

# GUI button
select_btn = CTkButton(master=app, text='Select file', command=openDir)
select_btn.place(relx=0.5, rely=0.45, anchor="center")

app.mainloop()

