l = input()
dih = {'a': 'ais',
       'e': 'enter',
       'i': 'inis',
       'o': 'omber',
       'u': 'uft'
       }
cv = ""
for p in l:
    cv = cv + dih.get(p, p)
print(cv)
