from math import fabs

pi = 3 
n = 2     
termos = 1 

while True:
    termo = (-1)**n * 4 / (n * (n+1) * (n+2))
    prev_pi = pi
    pi += termo
    termos += 1
    if fabs(pi - prev_pi) < 10**-5:
        break
    n += 1

print(pi)
print(termos)
