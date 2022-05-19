from turtle import Turtle

MOVE_STEP: int = 20


class Snake:
    segments: list[Turtle] = []

    is_alive = False

    def __init__(self):
        for i in range(2):
            t = Turtle("square")
            t.color("#e8e8e8")
            t.penup()
            t.setx(t.width() * -i)
            self.segments.append(t)
        self.is_alive = True

    def left(self):
        self.segments[0].left(90)

    def right(self):
        self.segments[0].right(90)

    def move(self):
        for idx in range(len(self.segments) - 1, -1, -1):
            seg = self.segments[idx]
            if idx == 0:
                seg.forward(MOVE_STEP)
            else:
                seg.goto(self.segments[idx - 1].pos())
            self.is_alive = self.is_alive and abs(seg.ycor()) < 280 and abs(seg.xcor()) < 280
