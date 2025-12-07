import random
import math
import turtle
pontos_total = 1000000
pontos_circulo = 0
raio = 250
random.seed()
turtle.clearscreen()
turtle.speed(1000)
turtle.ht()
turtle.forward(raio)
turtle.left(90)
turtle.forward(raio)
turtle.left(90)
turtle.forward(raio)
turtle.left(90)
turtle.forward(raio)
turtle.teleport(raio, 0)
turtle.seth(90)
turtle.circle(radius = raio)
for _ in range(pontos_total):
    x = random.random()
    y = random.random()
    turtle.teleport(x* raio, y* raio)
    if x*x + y*y <= 1:
        pontos_circulo += 1
        turtle.color('red')
    else:
        turtle.color('blue')
    turtle.dot()
pi = 4 * pontos_circulo / pontos_total
print(pi)

