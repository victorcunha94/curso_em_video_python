maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso é {}KG'.format(maior))
print('O MENOR peso que é {}KG'.format(menor))




