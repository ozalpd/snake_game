from turtle import Turtle

MOVE_STEP: int = 18
SCREEN_EDGE = 320
STARTING_SEGMENTS = 4
COLOR = "#E6E6E6"


class Snake:
    segments: list[Turtle] = []

    def __init__(self):
        self.add_segment((0, 0))  # adding head
        self.set_tail()
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

    def set_tail(self):
        for i in range(1, STARTING_SEGMENTS):
            self.add_segment((MOVE_STEP * -i, 0))

    def has_collision(self, any_turtle: Turtle) -> bool:
        collision = False
        for seg in self.segments[1:]:
            if seg.distance(any_turtle) < MOVE_STEP - 1:
                collision = True
                break
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

    def reset_game(self):
        self.head.goto(0, 0)
        self.head.setheading(0)
        for s in self.segments[1:]:
            self.segments.remove(s)
            s.hideturtle()
            s.goto(2560, 2560)
        self.turning = False
        self.is_alive = True
        self.set_tail()
