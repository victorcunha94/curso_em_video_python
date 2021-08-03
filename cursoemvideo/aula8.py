from math import sqrt, floor, trunc
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('O número {} tem raiz quadrada igual a {}'.format(num, trunc(raiz)))