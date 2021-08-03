frase = str(input('Digite uma frase: ')).strip()
fraseu = frase.upper()
print('A letra "A" aparececeu {} vezes'.format(fraseu.count('A')))
print('A primeira letra A apareceu na posição de índice {}'.format(fraseu.find('A')))
print('A posição da última letra A é {}'.format(fraseu.rfind('A')))

