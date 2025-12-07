import math
N = 10

numeros = list()

for _ in range(N):
    n = float(input())
    numeros.append(n)

soma = 0
for i in range(N):
    soma += numeros[i]
media = soma / N

sm_erros = 0
for i in range(N):
    sm_erros += (numeros[i] - media) ** 2
desvio = math.sqrt(sm_erros / (N - 1))
print(f"media: {media} desvio: {desvio}")

outliers = [numeros[i] for i in range(N) if numeros[i] < media - 3 * desvio or numeros[i] > media + 3 * desvio]
for num in outliers:
    print(f"{num} ")
