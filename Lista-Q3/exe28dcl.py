n = input()

exp = 0
sm = 0
for i in n[::-1]:
    sm += int(i) * 2 ** exp
    exp += 1
print(sm)
