produto = 1
n = int(input('Fatorial de: '))
for f in range(1, n+1):
    produto = produto*f
print('{}! = {}'.format(n, produto), end='')