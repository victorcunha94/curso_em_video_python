from datetime import date
ano = int(input('Digite o ano de nascimento do(a) atleta: '))
idade = date.today().year - ano
print('A idade do(a) atleta é {}'.format(idade))
if idade > 3 and idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR')
elif idade > 20:
    print('Categoria MASTER')
else:
    print('Ainda não tem idade para competir.')
