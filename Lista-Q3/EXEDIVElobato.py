from collections import defaultdict

tabela = defaultdict(lambda: [0, 0])
while True:
    linha = input()
    if linha == "Fim;0;0;Fim":
        break
    timeA, golsA, golsB, timeB = linha.split(';')
    golsA = int(golsA)
    golsB = int(golsB)

    tabela[timeA][1] += golsA - golsB
    tabela[timeB][1] += golsB - golsA
    if golsA > golsB:
        tabela[timeA][0] += 3
        tabela[timeB][0] += 0
    elif golsB > golsA:
        tabela[timeB][0] += 3
        tabela[timeA][0] += 0
    else:
        tabela[timeA][0] += 1
        tabela[timeB][0] += 1

tabela_ordenada = sorted(tabela.items(),key=lambda x: (x[1][0], x[1][1]), reverse=True)
print(f"{'Time':<20} {'Pontos':>6} {'Saldo': >6}")
for k, v in tabela_ordenada:
    print(f"{k:<20} {v[0]:>6} {v[1]: >6}")
