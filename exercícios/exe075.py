n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou:{n}')
print(f'O nove apareceu {n.count(9)} vezes')
if 3 not in n:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O primeiro valor 3 foi digitado na {n.index(3)+1}ª posição')
print(f'Os Valores pares digitados foram:', end=' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
