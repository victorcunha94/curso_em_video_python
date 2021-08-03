c = 1
impar = par = 0
while c != 0:
    c = int(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} pares e {} ímpares'.format(par, impar))





