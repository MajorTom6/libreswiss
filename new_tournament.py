from tkinter import Toplevel, IntVar, Label, Radiobutton, Button, messagebox
from window_functions import *
from new_random_swiss import *

def chosen(v,main):
    v=v.get()
    if v is 0:
        messagebox.showwarning("","You did not select an option.",parent=main)
    elif v is 1:
        new_random_swiss(main)
    else:
        print("Not implemented.")

def new_tournament(main):
    top = Toplevel(main)
    top.title("New Tournament")
    center_size(top,320,150)
    v = IntVar()
    Label(top, text='Select type:').grid(row=0,column=1) 
    Radiobutton(top, text='Random Single Swiss',    variable=v, value=1).grid(row=1,column=1)
    Radiobutton(top, text='!Rated Single Swiss!',   variable=v, value=2).grid(row=2,column=1)
    Radiobutton(top, text='!Random Double Swiss!',  variable=v, value=3).grid(row=3,column=1)
    Radiobutton(top, text='!Rated Double Swiss!',   variable=v, value=4).grid(row=4,column=1)
    Radiobutton(top, text='!Round Robin!',          variable=v, value=5).grid(row=5,column=1)
    Button(top, text='Okay', command=lambda: chosen(v,main)).grid(row=6,column=2)
    Button(top, text='Cancel', command=top.destroy).grid(row=6,column=0)

