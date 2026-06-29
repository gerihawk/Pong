from game.game import Game
from entities.window import Window
from entities.player import Player
from entities.ball import Ball
from entities.scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Window()
    left_player = Player("left")
    right_player = Player("right")
    ball = Ball()
    scoreboard = Scoreboard()
    game = Game(
        screen,
        left_player,
        right_player,
        ball,
        scoreboard,
    )
    game.run()