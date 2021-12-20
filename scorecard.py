from turtle import Turtle


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("yellow")
        self.hideturtle()
        self.current_score()

    def current_score(self):
        self.clear()
        self.goto(0,275)
        self.write(f"Score Board:- {self.score}, High Score:- {self.high_score}", True, align='center', font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.current_score()

    def high_sc(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.current_score()



