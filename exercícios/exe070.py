soma = caro = barato = cont = 0
maisbarato = ' '
print(10*'====')
print('      LOJA SUPER BARATÃO      ')
print(10*'====')
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    soma += preço
    cont += 1
    if cont == 1:
        barato = preço
        maisbarato = nome
    if preço < barato:
        barato = preço
        maisbarato = nome
    if preço > 1000:
        caro += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi {soma}')
print(f'{caro} custam mais que R$ 1000,00')
print(f'O produto mais barato é o {maisbarato}')

