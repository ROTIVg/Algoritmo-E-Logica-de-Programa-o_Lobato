palavra = input()
consoantes = ""
for letra in palavra:
    if letra() and letra.lower() not in "aeiou" and letra not in consoantes:
        consoantes += letra
print(list(consoantes)) 
