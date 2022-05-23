from turtle import Turtle
import random
import snake


class Food(Turtle):
    def __init__(self):
        self.contour = Turtle("circle")
        self.contour.color("#301830")
        self.contour.penup()
        self.contour.shapesize(stretch_wid=0.8, stretch_len=0.8)
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("#C020D8")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        tiles = int(snake.SCREEN_EDGE / snake.MOVE_STEP) - 1
        x = random.randint(-tiles, tiles) * snake.MOVE_STEP
        y = random.randint(-tiles, tiles) * snake.MOVE_STEP
        self.contour.goto(x, y)
        self.goto(x, y)
