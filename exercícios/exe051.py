a1 = int(input('Digite o primeiro termo na P.A: '))
r = int(input('Digite a razão da P.A: '))
an = a1 + (10 - 1)*r
for n in range(a1, an+1, r):
    print('{} '.format(n), end='->')