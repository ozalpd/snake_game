from turtle import Turtle

MOVE_STEP: int = 20


class Snake:
    segments: list[Turtle] = []

    def __init__(self):
        for i in range(2):
            t = Turtle("square")
            t.color("#e8e8e8")
            t.penup()
            t.setx(t.width() * -i)
            self.segments.append(t)
        self.is_alive = True
        self.head = self.segments[0]

    def is_heading_horizontally(self):
        return self.head.heading() % 180 == 0

    def is_heading_vertically(self):
        return self.head.heading() % 180 == 90

    def up(self):
        if self.is_heading_horizontally():
            self.head.setheading(90)

    def down(self):
        if self.is_heading_horizontally():
            self.head.setheading(270)

    def left(self):
        if self.is_heading_vertically():
            self.head.setheading(180)

    def right(self):
        if self.is_heading_vertically():
            self.head.setheading(0)

    def move(self):
        for idx in range(len(self.segments) - 1, -1, -1):
            seg = self.segments[idx]
            if idx == 0:
                seg.forward(MOVE_STEP)
            else:
                seg.goto(self.segments[idx - 1].pos())
        self.is_alive = self.is_alive and abs(self.head.ycor()) < 280 and abs(self.head.xcor()) < 280
