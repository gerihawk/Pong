"""
Controls the game loop and coordinates the interaction
between paddles, ball and scoreboard.
"""

from entities.window import Window
from entities.ball import Ball
from entities.player import Player
from entities.scoreboard import Scoreboard
from config import WINNING_SCORE


class Game:
    def __init__(
            self,
            screen: Window,
            left_player: Player,
            right_player: Player,
            ball: Ball,
            scoreboard: Scoreboard,
            ):
    
        self.left_player = left_player
        self.right_player = right_player
        self.screen = screen
        self.ball = ball
        self.scoreboard = scoreboard

    # ---------- Public API ----------
    def run(self) -> None:
        while not self.game_over:
            self.screen.update()
            self.update()

    def update(self) -> None:
        self.ball.move()
        self._check_collisions()
        self._handle_score()

    # --------- Internal helpers ---------
    def _check_collisions(self) -> None:
        if self.ball.collides_with(self.left_player.paddle):
            self.ball.bounce_off_paddle(self.left_player.paddle)
        if self.ball.collides_with(self.right_player.paddle):
            self.ball.bounce_off_paddle(self.right_player.paddle)

    def _handle_score(self) -> None:
        if self.ball.left_goal():
            self.scoreboard.increment_right()
            self.reset_round()
        elif self.ball.right_goal():
            self.scoreboard.increment_left()
            self.reset_round()

    # --------- Round management ---------
    def reset_round(self) -> None:
        self.ball.reset()
    
    def reset_game(self) -> None:
        self.ball.reset()
        self.scoreboard.reset()

    @property
    def game_over(self) -> bool:
        return self.scoreboard.left_score >= WINNING_SCORE or self.scoreboard.right_score >= WINNING_SCORE
    
  