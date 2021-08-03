soma = 0
produto = 1
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('''O que quer fazer com os números que digitou ?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Comparar 
[ 4 ] Novos números
[ 5 ] Encerrar
''')
p = int(input('Sua opção: '))
if p == 1:
    soma = n1 + n2
    print('A soma vale {}'.format(soma))
if p == 2:
    produto = n1*n2
    print('O produto vale {}'.format(produto))
if p == 3:
    if n1 > n2:
        print('{} é maior que {}'.format(n1, n2))
    if n1 < n2:
        print('{} é maior que {}'.format(n2, n1))
    else:
        print('São iguais.')
if p == 5:
    print('ENCERRADO')
while p == 4:
    soma = 0
    produto = 1
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('''O que quer fazer com os números que digitou ?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Comparar 
    [ 4 ] Novos números
    [ 5 ] Encerrar
    ''')
    p = int(input('Sua opção: '))
    if p == 1:
        soma = n1 + n2
        print('A soma vale {}'.format(soma))
    if p == 2:
        produto = n1 * n2
        print('O produto vale {}'.format(produto))
    if p == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        if n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('São iguais.')
    if p == 5:
        print('ENCERRADO')


