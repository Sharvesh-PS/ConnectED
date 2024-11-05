from turtle import Turtle


class Highscore(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,230)
        with open("high.txt","r") as fil:
            val = fil.readline()
            self.write(f"High Score: {val}", align="center", font=("Arial", 12, "normal"))