import turtle

from config import (
    WINDOW_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
)


class Window(turtle.Screen):
    """Represents the game window."""

    def __init__(self) -> None:
        super().__init__()
        self.title(WINDOW_TITLE)
        self.bgcolor(BACKGROUND_COLOR)
        self.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.tracer(0)