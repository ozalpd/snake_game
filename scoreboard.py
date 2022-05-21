from turtle import Turtle
import snake

FONT_SCORE = ('Arial', 18, 'bold')
FONT_BIG = ('Arial', 36, 'bold')
SCORE_POS = (0, snake.SCREEN_EDGE + 15)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_over(self):
        self.write_w_contour("GAME OVER", FONT_BIG, 0, 0)

    def write_w_contour(self, message: str, font, posX: int, posY: int):
        self.color("#401048")
        for x in range(-2, 3):
            for y in range(-2, 3):
                self.goto(posX + x, posY + y)
                self.write(message, align="center", font=font)
        self.goto(posX, posY)
        self.color("#e040f8")
        self.write(message, align="center", font=font)

    def write_score(self):
        self.clear()
        self.goto(SCORE_POS)
        self.color("#004080")
        self.write(f"Score: {self.score}", align="center", font=FONT_SCORE)
