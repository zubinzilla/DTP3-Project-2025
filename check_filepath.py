from customtkinter import *

# allow user to select directory from File Explorer
def openDir():
    filepath = filedialog.askdirectory()
    print(filepath)


app = CTk()
app.geometry('500x500')

set_appearance_mode("dark")
set_default_color_theme("green")

# GUI button
select_btn = CTkButton(master=app, text='Select file', command=openDir)
select_btn.place(relx=0.5, rely=0.45, anchor="center")


app.mainloop()

