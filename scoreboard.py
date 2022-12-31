from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#59595E')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.lives = 5
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Lives: {self.lives}", align='center', font=('arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()

    def end_game(self, win):
        self.clear()
        if win:
            self.write("You've Cleared the Screen! You Win!", align='center', font=('arial', 18, 'normal'))
        else:
            self.write("Game Over!", align='center', font=('arial', 18, 'normal'))
