import turtle

from config import (
    LEFT_PADDLE_X,
    RIGHT_PADDLE_X,
    PADDLE_SPEED,
    PADDLE_STRETCH_HEIGHT,
    PADDLE_STRETCH_WIDTH,
    PADDLE_SHAPE,
    PADDLE_COLOR,
    TOP_BORDER,
    BOTTOM_BORDER,
)


class Paddle:
    """Represents a paddle controlled by a player."""

    def __init__(self, side: str) -> None:
        self.sprite = turtle.Turtle()
        self.sprite.speed(PADDLE_SPEED)
        self.sprite.shape(PADDLE_SHAPE)
        self.sprite.color(PADDLE_COLOR)
        self.sprite.shapesize(
            stretch_wid=PADDLE_STRETCH_HEIGHT,
            stretch_len=PADDLE_STRETCH_WIDTH,
        )
        self.sprite.penup()
        if side == "left":
            self.sprite.goto(LEFT_PADDLE_X, 0)
        else:
            self.sprite.goto(RIGHT_PADDLE_X, 0)

    def move_up(self) -> None:
        y = self.sprite.ycor()
        if y < (TOP_BORDER - PADDLE_STRETCH_HEIGHT * 10):
            self.sprite.sety(y + PADDLE_SPEED)

    def move_down(self) -> None:
        y = self.sprite.ycor()
        if y > (BOTTOM_BORDER + PADDLE_STRETCH_HEIGHT * 10):
            self.sprite.sety(y - PADDLE_SPEED)

    @property
    def x(self) -> float:
        return self.sprite.xcor()

    @property
    def y(self) -> float:
        return self.sprite.ycor()
