from datetime import date
ano = int(input('Digite um ano para saber se é bisexto: '))
if ano == 0:
    ano = date.today().year
clas1 = ano % 4
clas2 = ano % 100
clas3 = ano % 400
if clas1 == 0 and clas2 != 0 or clas3 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))






