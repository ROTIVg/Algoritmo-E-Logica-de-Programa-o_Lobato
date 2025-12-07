binario = input()

decimal = 0
tamanho = len(binario)

for i in range(tamanho):
    digito = int(binario[-(i+1)])  
    decimal += digito * (2 ** i)

print(decimal)
