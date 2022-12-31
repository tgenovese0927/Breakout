from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('#59595E')
        self.shapesize(1, 5)
        self.speed('fastest')
        self.goto(position)

    def paddle_right(self):
        self.forward(50)

    def paddle_left(self):
        self.backward(50)
