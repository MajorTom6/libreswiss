from tkinter import Canvas, BOTH, YES
from window_functions import destroy_all
from random import shuffle
from math import ceil

def create_single_swiss(players,main):
    def create_plate(x,y,name):
        c.create_text(x+37,y+15,text=name)
        c.create_rectangle(x,y,x+75,y+25)
        c.create_line(x+75,y+12,x+85,y+12)

    destroy_all(main)
    c = Canvas(main)
    c.pack(fill=BOTH, expand=YES)

    shuffle(players)
    odd = False
    if(len(players)%2):
        odd = True

    i=int(ceil(len(players)/2))
    j=0;
    for x in range(i):
        if not odd:
            create_plate(25,25+x*75,players[j])
            j=j+1
            create_plate(25,55+x*75,players[j])
            j=j+1
            c.create_line(110,37+(x*75),110,67+(x*75))
        else:
            if j == i:
                create_plate(150,25+x*75,players[-1])
                break
            create_plate(25,25+x*75,players[j])
            j=j+1
            create_plate(25,55+x*75,players[j])
            j=j+1
            c.create_line(110,37+(x*75),110,67+(x*75))
