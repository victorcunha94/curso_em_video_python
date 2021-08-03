from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = (atual - ano)
if idade == 17:
    print('Compareça a junta militar mais próxima: ')
elif idade < 17:
    print('Ainda faltam {} anos para seu alistamento.'.format(17-idade))
elif idade > 17:
    print('Você passou da idade do alistamente, compareça a junta militar mais próxima.')
else:
    print('idade não válida.')


