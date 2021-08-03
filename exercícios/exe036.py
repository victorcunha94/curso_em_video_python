casa = float(input('Qual é o valor do financiamento? '))
salario = float(input('De quanto é seu aporte mensal? '))
tempo = int(input('Em quantos anos você deseja pagar o financiamento? '))
prest = casa / (tempo * 12)
if salario < (prest*0.30):
    print('Seu crédito foi recusado')
else:
    print('Seu crédito foi APROVADO!!')
    print('Sua prestação mensal será de R${:.2f}'.format(prest))
