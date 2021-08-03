pessoas = list()
dados = list()
totmaior = totmenor = 0
for p in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
for i in pessoas:
    if i[1] >= 18:
        totmaior += 1
        print(f'{i[0]} é maior de idade')
    else:
        totmenor += 1
        print(f'{i[0]} é menor de idade')

print(f'Ao todo temos {totmaior} maiores de idade e {totmenor} menores de idade')