n = input().lower()
l = {'0': 0,'1': 1,'2': 0,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'a': 10,'b': 11,'c': 12,'d': 13,'e': 14,'f': 15}
exp = 0
sm = 0
for i in n[::-1]:
    try:     
        sm += l.get(i, 0) * 16 ** exp
    except:
       print(f"o digito {i} nao existe no dict")
       exit()
    exp += 1
print(sm)
