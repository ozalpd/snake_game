import turtle

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
    screen.bgcolor("#2F373E")
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


def play_game():
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
    scoreboard.reset_score()


def play_again():
    snake.reset_game()
    play_game()


def close():
    if not snake.is_alive:
        screen.bye()


screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "d")
screen.onkeypress(snake.right, "Right")

screen.onkeypress(play_again, "y")
screen.onkeypress(close, "n")

play_game()

turtle.done()
