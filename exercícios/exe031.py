dist = float(input('Qual é a distância em KM da sua viagem? '))
pre1 = (dist*0.50)
pre2 = (dist*0.45)
if dist <= 200:
    print('O valor da viagem é R${:.2f} reais '.format(pre1))
else:
    print('O valor da viagem é R${:.2f} reais'.format(pre2))