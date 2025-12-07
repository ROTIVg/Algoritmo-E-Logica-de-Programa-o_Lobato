l = int(input())
a = int(input())

print('+' + '-' * (l-2) + '+')
for _ in range(a-2):
    print('|' + ' ' * (l-2) + '|')
if a > 1:
     print('+' + '-' * (l-2) + '+')
