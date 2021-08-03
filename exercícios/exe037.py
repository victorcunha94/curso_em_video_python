num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converte para binário
[ 2 ] Converte para octal
[ 3 ] Converte para hexadecimal''')
resp = int(input('Sua opção: '))
if resp == 1:
    print('{} em número binário é {} '.format(num, bin(num)))
elif resp == 2:
    print('{} em número octal é {}'.format(num, oct(num)))
elif resp == 3:
    print('{} em número hexadecimal {}'.format(num, (hex(num))))
else:
    print('Escolha inválida.')