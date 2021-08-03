num = []
while True:
    add = int(input('Digite um número: '))
    if add not in num:
        num.append(add)
        print('Adicionado com sucesso.')
    else:
        print('O número já foi adicionado.')
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()
    if 'n' in resp:
        break
num.sort()
print(num)
