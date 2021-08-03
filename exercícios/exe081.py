lista = []
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
        break
lista.sort()
print(f'Foram digitados {len(lista)} números')
print(f'A lista em ordem crescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')
