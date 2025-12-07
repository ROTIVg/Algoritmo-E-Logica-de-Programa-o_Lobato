m = float(input())
mv = int(input("qual o tempo de meia vida em sec"))
t = 0
while m >= 0.02:
    m = m / 2
    t += mv
dias, t = divmod(t, 24*3600)
horas, t = divmod(t, 3600)
minu, sec = divmod(t, 60)
print(f"os dias sao {dias} e as horas sao {horas} ", end="")
print(f"os minutos sao {minu} e os segundos {sec} para ter", end="")
print("menos que 0.02g de material")
