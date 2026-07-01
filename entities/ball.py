"""
Ball entity for the Pong game.
This module contains the Ball class, responsible for movement,
collision detection and goal detection.
"""

import turtle
import time

from entities.paddle import Paddle
from config import (
    TOP_BORDER,
    BOTTOM_BORDER,
    LEFT_BORDER,
    RIGHT_BORDER,
    BALL_SPEED,
    ROUND_RESET_DELAY,
    BALL_SHAPE,
    BALL_COLOR,
    BALL_ACCELERATION,
    BALL_PADDLE_COLLISION_DISTANCE,
)


class Ball:
    """Represents the ball used during the Pong game."""

    def __init__(self) -> None:
        self.sprite = turtle.Turtle()
        self.sprite.speed(0)
        self.sprite.shape(BALL_SHAPE)
        self.sprite.color(BALL_COLOR)
        self.sprite.penup()
        self.sprite.goto(0, 0)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self) -> None:
        self.sprite.setx(self.x + self.dx)
        self.sprite.sety(self.y + self.dy)

    def bounce_vertical(self) -> None:
        self.dy *= -1

    def bounce_horizontal(self) -> None:
        self.dx *= -1 * BALL_ACCELERATION

    def collides_with(self, paddle: Paddle) -> bool:
        return self.sprite.distance(paddle.sprite) < BALL_PADDLE_COLLISION_DISTANCE

    def check_wall_collision(self) -> None:
        if self.y >= TOP_BORDER or self.y <= BOTTOM_BORDER:
            self.bounce_vertical()

    def left_goal(self) -> bool:
        return self.x <= LEFT_BORDER

    def right_goal(self) -> bool:
        return self.x >= RIGHT_BORDER

    def reset(self) -> None:
        self.sprite.goto(0, 0)
        self.dx = -self.dx
        self.dy = BALL_SPEED if self.dy >= 0 else -BALL_SPEED
        time.sleep(ROUND_RESET_DELAY)

    @property
    def x(self) -> float:
        return self.sprite.xcor()

    @property
    def y(self) -> float:
        return self.sprite.ycor()
