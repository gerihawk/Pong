class Paddle():
    def __init__(self, x):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0) # Velocidad de animación
        self.turtle.shape("square") # Forma de la paleta
        self.turtle.color("white") # Color de la paleta
        self.turtle.shapesize(stretch_wid=5, stretch_len=1) # Tamaño de la paleta
        self.turtle.penup() # No dibujar al moverse
        self.turtle.goto(x, 0) # Posición inicial
    
    def go_up(self):
        y = self.turtle.ycor() # Obtener la coordenada y actual
        if y < 250: # Limitar el movimiento hacia arriba
            self.turtle.sety(y + 20) # Mover hacia arriba

    def go_down(self):
        y = self.turtle.ycor() # Obtener la coordenada y actual
        if y > -240: # Limitar el movimiento hacia abajo
            self.turtle.sety(y - 20) # Mover hacia abajo 