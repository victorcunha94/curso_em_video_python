m18 = masc = femi = 0
while True:
    print('====== Cadastre uma pessoa ========')
    sexo = seguir = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade > 18:
        m18 += 1
    if 'M' in sexo:
        masc += 1
    if 'F' in sexo and idade < 20:
        femi += 1
    while seguir not in 'NS':
        seguir = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if seguir == 'N':
        break
print(f'Foram cadastradas {m18} pessoas maiores de idade.')
print(f'{masc} são homens')
print(f'{femi} são mulheres com menos de 20 anos.')

