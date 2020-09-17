#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *

root = Tk()

style = Style()

style.configure('TButton', font=
('calibri', 10, 'bold'),
                foreground='black')

# set title

root.title("R0(t) for Covid-19")

# set window size
root.geometry('300x300')
# don't resize window
root.resizable(False, False)


def download_data():
    pass


def open_rstudio():
    pass


def source_files():
    pass


def open_pdf():
    pass


button_download = Button(root, text="Download data", command=download_data)
button_download.pack(side=TOP, expand=True, fill='both')

button_open_rstudio = Button(root, text="Open RStudio", command=open_rstudio)
button_open_rstudio.pack(side=TOP, expand=True, fill='both')

button_source_files = Button(root, text="Source files", command=source_files)
button_source_files.pack(side=TOP, expand=True, fill='both')

button_open_pdf = Button(root, text="Open dashboard (PDF)", command=open_pdf)
button_open_pdf.pack(side=TOP, expand=True, fill='both')

button_open_dashboard = Button(root, text="Open dashboard panel", command=open_pdf)
button_open_dashboard.pack(side=TOP, expand=True, fill='both')

root.mainloop()
