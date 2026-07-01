"""
Controls the game loop and coordinates the interaction
between paddles, ball and scoreboard.
"""

import time
import turtle

from entities.window import Window
from entities.ball import Ball
from entities.player import Player
from entities.scoreboard import Scoreboard
from config import (
    WINNING_SCORE,
    WINNER_FONT,
    WINNER_MESSAGE_Y,
    MESSAGE_COLOR,
    FPS,
)


class Game:
    """
    Coordinates the game loop and manages the interaction
    between all game entities.
    """

    def __init__(
        self,
        screen: Window,
        left_player: Player,
        right_player: Player,
        ball: Ball,
        scoreboard: Scoreboard,
    ) -> None:

        self.screen = screen
        self.left_player = left_player
        self.right_player = right_player
        self.ball = ball
        self.scoreboard = scoreboard
        self.message: turtle.Turtle = self._create_message_turtle()

    # ---------- Public API ----------
    def run(self) -> None:
        while not self.game_over:
            self.screen.update()
            self._update()
            time.sleep(1 / FPS)
        self._show_winner()

    def reset_round(self) -> None:
        """Starts a new round after a goal."""
        self.ball.reset()

    @property
    def game_over(self) -> bool:
        return (
            self.scoreboard.left_score >= WINNING_SCORE
            or self.scoreboard.right_score >= WINNING_SCORE
        )

    # --------- Internal helpers ---------
    def _update(self) -> None:
        self.ball.move()
        self.ball.check_wall_collision()
        self._check_collisions()
        self._handle_score()

    def _check_collisions(self) -> None:
        if self.ball.collides_with(self.left_player.paddle):
            self.ball.bounce_horizontal()
        elif self.ball.collides_with(self.right_player.paddle):
            self.ball.bounce_horizontal()

    def _handle_score(self) -> None:
        if self.ball.left_goal():
            self.scoreboard.increment_right()
            self.reset_round()
        elif self.ball.right_goal():
            self.scoreboard.increment_left()
            self.reset_round()

    def _show_winner(self) -> None:
        """Displays the winner when the match ends."""

        winner = (
            "Left Player Wins!"
            if self.scoreboard.left_score >= WINNING_SCORE
            else "Right Player Wins!"
        )

        self.message.clear()
        self.message.goto(0, WINNER_MESSAGE_Y)
        self.message.write(
            winner,
            align="center",
            font=WINNER_FONT,
        )

    def _create_message_turtle(self) -> turtle.Turtle:
        """Creates the turtle used to display game messages."""
        message = turtle.Turtle()
        message.hideturtle()
        message.penup()
        message.color(MESSAGE_COLOR)
        return message

    def _register_controls(self) -> None:
        """Registers the keyboard controls for the game."""
        self.screen.listen()
        self.screen.onkeypress(self.left_player.move_up, "w")
        self.screen.onkeypress(self.left_player.move_down, "s")
        self.screen.onkeypress(self.right_player.move_up, "up")
        self.screen.onkeypress(self.right_player.move_down, "down")
