####*** event handing ***####

## mouse button ##

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x900")

def left_button(event):
    messagebox.showinfo("info","left button clicked")
    
    
def right_button(event):
    messagebox.showinfo("info","right button clicked")
    
root.bind("<Button-1>",left_button)
root.bind("<Button-3>",right_button)

root.mainloop()
