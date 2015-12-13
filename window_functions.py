def center_size(win,width,height):
    win.update_idletasks()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def destroy_all(main):
    for child in main.winfo_children():
        if child.winfo_class() == "Canvas":
            child.destroy()
        elif child.winfo_class() == "Toplevel":
            child.destroy()
