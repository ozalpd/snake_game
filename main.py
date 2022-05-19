from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Pop's Snake Game")
screen.bgcolor("#282828")
snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

while snake.is_alive:
    snake.move()
    screen.update()
    time.sleep(0.25)

screen.exitonclick()
