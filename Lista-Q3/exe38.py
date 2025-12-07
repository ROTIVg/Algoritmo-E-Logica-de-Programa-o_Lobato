total = int(input("Quantas figurinhas tem no álbum? "))

fig1 = []
while True:
    n = int(input("Quais figurinhas a criança 1 tem (-1 para parar)"))
    if n == -1:
        break
    fig1.append(n)

fig2 = []
while True:
    n = int(input("Quais figurinhas a criança 2 tem (-1 para parar)"))
    if n == -1:
        break
    fig2.append(n)

faltam1 = []
for i in range(1, total+1):
    if i not in fig1:
        faltam1.append(i)

faltam2 = []
for i in range(1, total+1):
    if i not in fig2:
        faltam2.append(i)

rep1 = []
for i in set(fig1):
    if fig1.count(i) > 1:
        rep1.append(i)

rep2 = []
for i in set(fig2):
    if fig2.count(i) > 1:
        rep2.append(i)

peg1 = []
for i in set(fig2):
    if i not in fig1:
        peg1.append(i)

peg2 = []
for i in set(fig1):
    if i not in fig2:
        peg2.append(i)

print("\nCriança 1")
print("Figurinhas que faltam:", ", ".join(str(x) for x in faltam1))
if rep1:
    print("Figurinhas repetida:", ", ".join(str(x) for x in rep1))
else:
    print("Figurinhas repetida: nenhuma")
if peg1:
    print("Figurinhas que pode pegar da Criança 2:", ", ".join(str(x) for x in peg1))
else:
    print("Figurinhas que pode pegar da Criança 2: nenhuma")

print("\nCriança 2")
print("Figurinhas que faltam:", ", ".join(str(x) for x in faltam2))
if rep2:
    print("Figurinhas repetida:", ", ".join(str(x) for x in rep2))
else:
    print("Figurinhas repetida: nenhuma")
if peg2:
    print("Figurinhas que pode pegar da Criança 1:", ", ".join(str(x) for x in peg2))
else:
    print("Figurinhas que pode pegar da Criança 1: nenhuma")
