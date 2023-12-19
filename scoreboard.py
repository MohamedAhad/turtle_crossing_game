from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.level_count()


    def level_count(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.level_count()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

