nome = str(input('Digite seu nome: '))
if nome == 'Victor' or nome == 'Angela':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'José':
    print('Seu nome é muito comum no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))

