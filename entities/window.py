import turtle

from config import (
    WINDOW_TITLE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
)


class Window:
    """Represents the game window."""

    def __init__(self) -> None:
        self._screen = turtle.Screen()
        self._screen.title(WINDOW_TITLE)
        self._screen.bgcolor(BACKGROUND_COLOR)
        self._screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._screen.tracer(0)

    def update(self) -> None:
        self._screen.update()

    def listen(self) -> None:
        self._screen.listen()

    def onkeypress(self, func, key: str) -> None:
        self._screen.onkeypress(func, key)

    def mainloop(self) -> None:
        self._screen.mainloop()

    def clear(self) -> None:
        self._screen.clear()

    def bye(self) -> None:
        self._screen.bye()
