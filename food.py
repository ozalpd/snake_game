from turtle import Turtle
import random
import snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("#a0e8f8")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        tiles = int(snake.SCREEN_EDGE / snake.MOVE_STEP) - 1
        x = random.randint(-tiles, tiles) * snake.MOVE_STEP
        y = random.randint(-tiles, tiles) * snake.MOVE_STEP
        self.goto(x, y)
