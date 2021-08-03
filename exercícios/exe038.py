primeiro = float(input('Primeiro valor: '))
segundo = float(input('Segundo valor: '))
if primeiro < segundo:
    print('{} é maior que {}'.format(segundo, primeiro))
elif primeiro > segundo:
    print('{} é maior que {}'.format(primeiro, segundo))
else:
    print('{} e {} são iguais! ')