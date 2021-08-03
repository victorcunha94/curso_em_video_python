lista = []
while True:
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
        break
print(f'A lista completa é {lista}')
impares = lista[:]
pares = lista[:]
for v, c in enumerate(lista):
    if c % 2 == 0:
        impares.remove(c)
print(f'Ímpares: {impares}')

for v, c in enumerate(lista):
    if c % 2 != 0:
        pares.remove(c)
print(f'Pares: {pares}')


