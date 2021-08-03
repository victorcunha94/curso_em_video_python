a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
contador = 1
p = 10
total = 0
while p != 0:
    total += p
    while contador <= total:
        termo += r
        print('{} - '.format(termo), end='')
        contador += 1
    print('PAUSA')
    p = int(input('Quantos termos a mais? '))
print('FIM')