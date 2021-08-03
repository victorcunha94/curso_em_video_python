número = 1
soma = 0
while número != 999:
    número = int(input('Digite um número: '))
    if número != 999:
        soma += número
    else:
        print('FIM - ', end='')
print('A soma dos termos digitas é {}'.format(soma), end='')
