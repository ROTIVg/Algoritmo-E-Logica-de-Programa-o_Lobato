import math
N = 10

numeros = list()

for _ in range(N):
    n = float(input())
    numeros.append(n)

soma = 0
for i in range(N):
    soma = soma = numeros[i]
media = soma / N

sm_erros = 0
for i in range(N):
    sm_erros = sm_erros + (numeros[i] - media) ** 2
desvio = math.sqrt(sm_erros / (N - 1))
print(f" media: {media} desvio: {desvio}
    for i in range(N):
      if numeros[i] < media - 3 * desvio or \
         numeros[i] > media + 3 * desvio:
            print(f"{numeros} ")
