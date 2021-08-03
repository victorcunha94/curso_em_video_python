num = int(input('Digite um número entre 1 e 9999: '))
mil = (num // 1000) % 10
cen = (num // 100) % 10
dez = (num // 10) % 10
uni = (num // 1) % 10
print('Milhar {}'.format(mil))
print('Centena {}'.format(cen))
print('Dezena {}'.format(dez))
print('Unidade {}'.format(uni))
