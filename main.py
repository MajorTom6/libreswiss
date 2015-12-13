from tkinter import Tk, Menu
from new_tournament import *
from new_random_swiss import *
from create_single_swiss import *

main = Tk()

main.title("LibreSwiss")
center_size(main,640,480)

menu_bar = Menu(main)
menu_file = Menu(menu_bar,tearoff=0)
menu_edit = Menu(menu_bar,tearoff=0)

menu_bar.add_cascade(label="File", menu = menu_file)
menu_file.add_command(label="New", command = lambda:new_tournament(main))
menu_file.add_command(label="Save")
menu_file.add_command(label="Quit", command=main.destroy)

menu_bar.add_cascade(label="Edit", menu = menu_edit)
menu_edit.add_command(label="Scramble")

main.config(menu=menu_bar)
main.mainloop()
