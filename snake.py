from turtle import Turtle

MOVE_STEP: int = 18
SCREEN_EDGE = 320
STARTING_SEGMENTS = 4
COLOR = "#f8a0b8"


class Snake:
    segments: list[Turtle] = []

    def __init__(self):
        for i in range(STARTING_SEGMENTS):
            self.add_segment((MOVE_STEP * -i, 0))
        self.is_alive = True
        self.head = self.segments[0]
        self.turning = False

    def add_segment(self, pos):
        t = Turtle("square")
        t.color(COLOR)
        t.penup()
        t.shapesize(stretch_wid=0.8, stretch_len=0.8)
        t.goto(pos)
        self.segments.append(t)

    def has_collision(self, any_turtle: Turtle) -> bool:
        collision = False
        for seg in self.segments[1:]:
            if self.head.distance(seg) < MOVE_STEP - 1:
                collision = True
        return collision

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def is_heading_horizontally(self):
        return self.head.heading() % 180 == 0

    def is_heading_vertically(self):
        return self.head.heading() % 180 == 90

    def up(self):
        if not self.turning and self.is_heading_horizontally():
            self.head.setheading(90)
            self.turning = True

    def down(self):
        if not self.turning and self.is_heading_horizontally():
            self.head.setheading(270)
            self.turning = True

    def left(self):
        if not self.turning and self.is_heading_vertically():
            self.head.setheading(180)
            self.turning = True

    def right(self):
        if not self.turning and self.is_heading_vertically():
            self.head.setheading(0)
            self.turning = True

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            seg = self.segments[idx]
            seg.goto(self.segments[idx - 1].pos())
        self.head.forward(MOVE_STEP)
        self.turning = False
        self.is_alive = not self.has_collision(self.head)

        # detecting collision with edge
        if abs(self.head.ycor()) > SCREEN_EDGE or abs(self.head.xcor() + 8) > SCREEN_EDGE:
            self.is_alive = False
