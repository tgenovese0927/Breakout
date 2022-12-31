from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('#59595E')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.reset_position()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(x=0, y=-240)
        self.y_move = 10
        self.move_speed = 0.1
