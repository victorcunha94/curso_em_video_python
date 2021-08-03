from datetime import date
maiores = 0
menores = 0
a = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (a - ano) >= 18:
        maiores += 1
    elif (a - ano) < 18:
        menores += 1
print('{} pessoas são maiores de idade e {} é menor'.format(maiores, menores))
