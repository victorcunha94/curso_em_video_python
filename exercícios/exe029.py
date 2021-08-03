km = int(input('Qual é a velocidade do carro? '))
multa = (km - 80)*7
if km <= 80 :
    print('Muito bem, siga com segurança!')
else:
    print('Você foi multado')
    print('Você pagará por exceder o limite de velocidade R$ {} reais'.format(multa))