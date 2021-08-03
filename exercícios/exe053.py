frase = str(input('Digite uma frase: ')).lower().split()
frase1 = str(''.join(frase))
a = frase1[::-1]
if a == frase1:
    print('{} é PALÍNDROMO'.format(frase))
else:
    print('{} NÃO é palíndromo.'.format(frase))
