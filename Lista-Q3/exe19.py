dive = int(input())
div = int(input())

if div == 0:
    print("erro")
else:
    q = 0
    r = dive
    while r >= div:
        r -= div
        q += 1
    print(q)
    print(r)
