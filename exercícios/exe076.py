listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)
print(40*'-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40 * '-')
for k in range(0, len(listagem)):
    if k % 2 == 0:
        print(f'{listagem[k]:.<30}', end=' ')
    else:
        print(f'R${listagem[k]:>7.2f}')
print(40 * '-')