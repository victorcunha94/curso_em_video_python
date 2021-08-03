lista = list()
for n in range(5):
    lista.append(int(input(f'Digite um número para posição {n} : ')))
mai = max(lista)
men = min(lista)
print(f'O maior valor digitado foi {mai} na posição : ', end=' ')
for i, k in enumerate(lista):
    if k == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} na posição: ', end=' ')
for j, q in enumerate(lista):
    if q == men:
        print(f'{j}...', end=' ')