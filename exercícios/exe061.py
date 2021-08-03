a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = 1
while termos < 10:
    a1 = a1 + r
    print('{}'.format(a1), end=' → ')
    termos += 1

