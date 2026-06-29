import turtle

# Configurar la ventana
class Ventana():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Arcade Pong")
        self.screen.setup(width=800, height=600) # Tamaño de la ventana
        self.screen.bgcolor("black") # Color de fondo
        self.screen.listen() # Escuchar eventos de teclado


# Configurar las paletas
class Paleta():
    def __init__(self, x):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0) # Velocidad de animación
        self.turtle.shape("square") # Forma de la paleta
        self.turtle.color("white") # Color de la paleta
        self.turtle.shapesize(stretch_wid=5, stretch_len=1) # Tamaño de la paleta
        self.turtle.penup() # No dibujar al moverse
        self.turtle.goto(x, 0) # Posición inicial
    
    def subir(self):
        y = self.turtle.ycor() # Obtener la coordenada y actual
        if y < 250: # Limitar el movimiento hacia arriba
            self.turtle.sety(y + 20) # Mover hacia arriba

    def bajar(self):
        y = self.turtle.ycor() # Obtener la coordenada y actual
        if y > -240: # Limitar el movimiento hacia abajo
            self.turtle.sety(y - 20) # Mover hacia abajo    

# Configurar la pelota
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
    

# Configurar el marcador
class Marcador():
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


def main():
    ventana = Ventana()
    ventana.screen.tracer(0)
    paleta_izq = Paleta(-350)
    paleta_der = Paleta(350)
    pelota = Pelota()
    marcador = Marcador()

    # Asignar las teclas para mover la paleta izquierda
    ventana.screen.onkeypress(paleta_izq.subir, "w") # Tecla "w" para subir
    ventana.screen.onkeypress(paleta_izq.bajar, "s") # Tecla "s" para bajar
    ventana.screen.onkeypress(paleta_der.subir, "Up") # Tecla "up" para subir
    ventana.screen.onkeypress(paleta_der.bajar, "Down") # Tecla "down" para bajar

    # Bucle principal del juego
    while True:
        ventana.screen.update()
        # Mover la pelota
        pelota.mover()
        # Rebote de la pelota en los bordes superior e inferior
        pelota.comprobar_bordes = pelota.sprite.ycor()
        if pelota.comprobar_bordes > 290 or pelota.comprobar_bordes < -290:
            pelota.rebotar_vertical()
        # Rebote de la pelota en las paletas
        pelota.comprobar_colision(paleta_izq) = paleta_izq.sprite.ycor()
        pelota.comprobar_colision(paleta_der) = paleta_der.sprite.ycor()
        if (pelota.sprite.xcor() > 340 and pelota.sprite.xcor() < 350) and (pelota.sprite.ycor() < pelota.comprobar_colision(paleta_der) + 50 and pelota.sprite.ycor() > pelota.comprobar_colision(paleta_der) - 50):
            pelota.rebotar_horizontal()
            pelota.dx *= 1.05  # Aumentar la velocidad de la pelota al rebotar en la paleta derecha
        if (pelota.sprite.xcor() < -340 and pelota.sprite.xcor() > -350) and (pelota.sprite.ycor() < pelota.comprobar_colision(paleta_izq) + 50 and pelota.sprite.ycor() > pelota.comprobar_colision(paleta_izq) - 50):
            pelota.rebotar_horizontal()
            pelota.dx *= 1.05  # Aumentar la velocidad de la pelota al rebotar en la paleta izquierda
        # Actualizar el marcador si la pelota sale por los lados
        pelota.comprobar_punto = pelota.sprite.xcor()
        if pelota.comprobar_punto > 390:
            marcador.puntos_izq += 1
            marcador.actualizar_marcador()
            pelota.reiniciar()
        if pelota.comprobar_punto < -390:
            marcador.puntos_der += 1
            marcador.actualizar_marcador()
            pelota.reiniciar()


if __name__ == "__main__":
    main()
