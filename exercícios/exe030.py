num = int(input('Digite um número: '))
resto = (num % 2)
if resto == 0:
    print('{} é um número par'.format(num))
else:
    print('{} é um número ímpar'.format(num))
