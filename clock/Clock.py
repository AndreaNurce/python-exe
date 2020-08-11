from tkinter import *
import time
import sys

def ca():
    curr_time = time.strftime("%H:%M:%S")
    clock.config(text=curr_time)
    clock.after(100, ca)


root = Tk()
root.title("Time by Andrea")
clock = Label(root, font={"times", 200, "bold"}, bg='white')
clock.grid(row=0, column=1)
ca()
root.mainloop()