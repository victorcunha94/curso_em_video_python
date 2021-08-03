valores = [[2], [3]]

for i in range(7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'O todo é {valores}')
print(f'Os valores pares digitados são {valores[0].sort()}')
print(f'Os valores ímpares digitados são {valores[1].sort()}')
