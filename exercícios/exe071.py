valor = int(input('Qual valor deseja sacar? R$ '))
total = valor
ced = 50
cedtotal = 0
while True:
    if total >= ced:
        total -= ced
        cedtotal += 1
    else:
        if cedtotal > 0:
            print(f'São {cedtotal} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
