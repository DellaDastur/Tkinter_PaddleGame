from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:

    #takes the parameter of the canvas and color of the ball
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass
        
ball = Ball(canvas, 'red')

# this is the main loop of our game
# we need to add an animation loop to stop the window from closing immediately
# Central part of the game that controls what it does
# This loop for the moment just tells tkinter to redraw the screen.
while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

