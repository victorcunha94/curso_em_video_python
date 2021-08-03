num = int(input('Digite um número: '))
divisores = 0
for x in range(1, num+1):
    if num % x == 0:
        divisores += 1
if divisores > 2:
    print('{} não é PRIMO.'.format(num))
if divisores == 2:
    print('{} é PRIMO'.format(num))