frase = str(input('Digite uma frase: '))
frase1 = frase.lower().split()
frase2 = ''.join(frase1)
inverso = ''
for i in range(len(frase2) - 1, -1, -1):
    inverso += frase2[i]
print('O inverso da frase {} é {}'.format(frase2, inverso))
if inverso == frase2:
    print('Portando é um PALÍNDROMO.')
else:
    print('Portanto NÃO é um palíndromo.')
