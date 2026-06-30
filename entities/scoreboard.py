import turtle

from config import (
    SCOREBOARD_FONT,
    SCOREBOARD_Y,
)
class Scoreboard:
    """Displays and manages the game score."""

    def __init__(self) -> None:
        self.sprite = turtle.Turtle()
        self.sprite.hideturtle()
        self.sprite.penup()
        self.sprite.goto(0, SCOREBOARD_Y)
        self.sprite.color("white")
        self._draw()
        self.left_score = 0
        self.right_score = 0
        
    def increment_left(self) -> None:
        self.left_score += 1
        self._draw()

    def increment_right(self) -> None:
        self.right_score += 1
        self._draw()

    def reset(self) -> None:
        self.left_score = 0
        self.right_score = 0
        self._draw()

    def _draw(self) -> None:
        self.sprite.clear()
        self.sprite.write(f'{self.left_score} - {self.right_score}',
                          align="center",
                          font=SCOREBOARD_FONT
                          )