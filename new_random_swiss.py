from tkinter import Toplevel, Label, Entry, Button, Scrollbar, Listbox, EXTENDED, END
from window_functions import center_size
from create_single_swiss import create_single_swiss

def new_random_swiss(main):
    players = []
    def add_player(event):
        if e.get() is "":
            return
        players.append(e.get())
        Lb.delete(0,END)
        for x in players:
            Lb.insert(0,x)
        e.delete(0,END)

    def remove_player():
        l=len(players)-1
        if Lb.curselection():
            for x in Lb.curselection():
                Lb.delete(x)
                players.pop(l-x)
        else:
            Lb.delete(0)
            players.pop(-1)
        Lb.delete(0,END)
        for x in players:
            Lb.insert(0,x)


    top = Toplevel(main)
    top.title("New Random Swiss")
    top.bind("<Return>",add_player)
    center_size(top,360,180)
    Label(top, text='Name:').grid(row=0,column=0)
    e = Entry(top,width=12)
    e.grid(row=0,column=1)
    e.focus_force()
    Button(top,text='Add',	command=lambda:add_player(None)			).grid(row=1,column=0)
    Button(top,text='Remove',	command=remove_player				).grid(row=1,column=1)
    Button(top,text='Cancel',	command=top.destroy				).grid(row=2,column=0)
    Button(top,text='Finish',	command=lambda:create_single_swiss(players,main)).grid(row=2,column=1)
    Sb = Scrollbar(top)
    Sb.grid(row=0,column=3,rowspan=3)
    Lb = Listbox(top,selectmode=EXTENDED,yscrollcommand=Sb.set)
    Lb.grid(row=0,rowspan=3,column=2)
    Sb.config(command=Lb.yview)
