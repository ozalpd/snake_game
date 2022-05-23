from turtle import Turtle
import snake

FONT_SCORE = ('Arial', 18, 'bold')
FONT_BIG = ('Arial', 36, 'bold')
HISCORE_POS = (180, snake.SCREEN_EDGE + 15)
SCORE_POS = (-220, snake.SCREEN_EDGE + 15)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.hi_score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        if self.score > self.hi_score:
            self.hi_score = self.score
        self.write_score()

    def write_over(self):
        self.write_w_contour("GAME OVER", FONT_BIG, 0, 0)
        self.goto(0, -50)
        self.write("Play again? Hit Y or N: ", align="center", font=FONT_SCORE)

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
        self.color("#004080")
        self.goto(HISCORE_POS)
        self.write(f"Hi Score: {self.hi_score}", align="center", font=FONT_SCORE)
        self.goto(SCORE_POS)
        self.write(f"Score: {self.score}", align="center", font=FONT_SCORE)

    def reset_score(self):
        self.score = 0
        # TODO: save hi score here
