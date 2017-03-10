from tkinter import *
import random
import time

WIDTH = 600
HEIGHT = 500

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="white")
tk.title("Moving ball")
canvas.pack()

class Ball:
    def __init__(self):
        self.size = 50
        self.shape = canvas.create_oval(0, 0, self.size, self.size, fill = 'red')
        self.speedx = random.randrange(5, 15)
        self.speedy = random.randrange(5, 15)

    def update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1


ball_list = []
ball_list.append(Ball())
while True:
    for ball in ball_list:
        ball.update()
    tk.update()
    time.sleep(0.01)
