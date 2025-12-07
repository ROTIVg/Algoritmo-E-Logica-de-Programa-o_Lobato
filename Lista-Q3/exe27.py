n = int(input())
m = int(input())
d = 0
if m < n:
    d = m
else:
    d = n
while m % d != 0 or n % d != 0:
    d = d-1
print(d)
