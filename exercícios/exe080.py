lista = []
for k in range(5):
    add = int(input('Digite um número: '))
    if k == 0 or add > lista[-1]:
        lista.append(add)
    else:
        pos = 0
        while pos < len(lista):
            if add <= lista[pos]:
                lista.insert(pos, add)
                break
            pos += 1
print(lista)