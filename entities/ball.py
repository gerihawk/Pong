class Pelota():
    def __init__(self):
        self.sprite = turtle.Turtle()
        self.sprite.speed(0) # Velocidad de animación
        self.sprite.shape("circle") # Forma de la pelota
        self.sprite.color("white") # Color de la pelota
        self.sprite.penup() # No dibujar al moverse
        self.sprite.goto(0, 0) # Posición inicial
        self.dx = 2 # Velocidad de movimiento en x
        self.dy = 2 # Velocidad de movimiento en y 
    def mover(self):
        self.sprite.setx(self.sprite.xcor() + self.dx)
        self.sprite.sety(self.sprite.ycor() + self.dy)
    def rebotar_vertical(self):
        self.dy *= -1
    def rebotar_horizontal(self):
        self.dx *= -1
    def reiniciar(self):
        self.sprite.goto(0, 0)
        self.wait(1) # Esperar 1 segundo antes de reiniciar
        self.rebotar_horizontal()
    