from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-285, 285)
        self.pendown()
        self.width(5)
        self.goto(285, 285)
        self.goto(285,-285)
        self.goto(-285,-285)
        self.goto(-285,285)
        self.penup()