pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c = str(input('Deseja continuar?[S/N] ')).lower()
    if c == 'n':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f' [{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso}Kg de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f' [{p[0]}]', end='')
print()
