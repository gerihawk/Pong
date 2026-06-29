class Scoreboard():
    def __init__(self):
        self.marcador = turtle.Turtle()
        self.marcador.speed(0)
        self.marcador.color("white")
        self.marcador.penup()
        self.marcador.hideturtle()
        self.marcador.goto(0, 260)
        self.puntos_izq = 0
        self.puntos_der = 0
        self.actualizar_marcador()
    def actualizar_marcador(self):
        self.marcador.clear()
        self.marcador.write(f"Jugador 1: {self.puntos_izq}  Jugador 2: {self.puntos_der}", align="center", font=("Courier", 24, "normal"))