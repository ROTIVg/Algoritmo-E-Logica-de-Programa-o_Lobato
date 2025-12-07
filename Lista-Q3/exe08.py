num = input()
digs = ["zero ", "um ", "dois ", "tres ", "quatro ", "cinco ",  "seis ", "sete ", "oito ", "nove "]
cr = []
print(num)
for dig in num[::-1]:
    cr.append(digs[int(dig)])
for c in cr:
    print(c)
        
