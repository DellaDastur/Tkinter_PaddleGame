from tkinter import *
import random
import time

tk = Tk()

tk.title("Game")

# window cannot change horizontally or vertically
tk.resizable(0, 0)
# canvas in the window is made the topmost object
tk.wm_attributes("-topmost", 1)

#bd and thickness is to make sure there is no border
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)

#canvas to size itself in the window
canvas.pack()

#initialize itself for the animation
tk.update()