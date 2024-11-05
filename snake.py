from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180 , 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def add_segment(self, i):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(i)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for j in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[j - 1].xcor()
            new_y = self.segments[j - 1].ycor()
            self.segments[j].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

