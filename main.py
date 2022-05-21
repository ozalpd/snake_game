from scoreboard import ScoreBoard
from turtle import Screen, Turtle
from snake import Snake, COLOR, MOVE_STEP, SCREEN_EDGE
from food import Food
import time

screen = Screen()


def set_screen():
    border_thickness = 20
    screen.tracer(0)
    scr_width = (SCREEN_EDGE + (2 * border_thickness)) * 2
    scr_height = (SCREEN_EDGE + (3 * border_thickness)) * 2
    screen.setup(width=scr_width, height=scr_height)
    screen.title("Pop's Snake Game")
    screen.bgcolor("#282828")
    drawer: Turtle = Turtle()
    drawer.penup()
    drawer.hideturtle()
    drawer.color(COLOR)
    drawer.pensize(border_thickness)
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, -SCREEN_EDGE - border_thickness)
    drawer.pendown()
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, SCREEN_EDGE + border_thickness)
    drawer.goto(SCREEN_EDGE + border_thickness, SCREEN_EDGE + border_thickness)
    drawer.goto(SCREEN_EDGE + border_thickness, -SCREEN_EDGE - border_thickness)
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, -SCREEN_EDGE - border_thickness)
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, -SCREEN_EDGE - (2 * border_thickness))
    drawer.goto(SCREEN_EDGE + border_thickness, -SCREEN_EDGE - (2 * border_thickness))
    drawer.goto(SCREEN_EDGE + border_thickness, SCREEN_EDGE + (2 * border_thickness))
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, SCREEN_EDGE + (2 * border_thickness))
    drawer.goto(-SCREEN_EDGE - border_thickness - 7, 0)


set_screen()
snake = Snake()

food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

screen.update()

while snake.is_alive:
    snake.move()
    scoreboard.write_score()
    screen.update()
    if snake.head.distance(food) < MOVE_STEP / 2:
        food.refresh()
        snake.extend()
        while snake.has_collision(food):
            food.refresh()
        scoreboard.increase_score()
    screen.update()
    time.sleep(0.25)

scoreboard.write_over()
screen.exitonclick()
