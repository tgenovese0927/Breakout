from turtle import Turtle
import random

COLORS = ['#59595E', '#9191E3', '#3C3C5E', '#A1A1AB', '#8867F4', '#1E0375']


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.shapesize(1.5, 3)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=x_cor, y=y_cor)

        self.left = self.xcor() - 35
        self.right = self.xcor() + 35
        self.upper = self.ycor() + 15
        self.lower = self.ycor() - 15


class Wall:
    def __init__(self):
        self.y_start = 60
        self.y_end = 240
        self.wall = []
        self.all_lanes()

    def lanes(self, y_cor):
        for a in range(-360, 400, 64):
            bricks = Brick(a, y_cor)
            self.wall.append(bricks)

    def all_lanes(self):
        for a in range(self.y_start, self.y_end, 32):
            self.lanes(a)


