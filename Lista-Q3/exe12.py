import random
import math
random.seed()
pontos_total = 1000000
pontos_circulo = 0

for _ in range(pontos_total):
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        pontos_circulo += 1

pi = 4 * pontos_circulo / pontos_total
print(pi)

