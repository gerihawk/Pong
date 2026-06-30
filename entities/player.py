from entities.paddle import Paddle

class Player:
    """Represents one player in the Pong game."""
    def __init__(self, side: str) -> None:
        self.side = side
        self.paddle = Paddle(side)
    
    def move_up(self) -> None:
        self.paddle.move_up()
    
    def move_down(self) -> None:
        self.paddle.move_down()