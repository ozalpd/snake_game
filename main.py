from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pop's Snake Game")
screen.bgcolor("#282828")
screen.tracer(0)
snake = Snake()

screen.update()

test_idx = 0
while snake.is_alive:
    snake.move()

    test_idx += 1
    if test_idx % 17 == 0:
        snake.left()
    elif test_idx % 11 == 0:
        snake.right()

    screen.update()
    time.sleep(0.25)

screen.exitonclick()
