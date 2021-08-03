media_grupo = 0
soma_idade = 0
maioridadehomem = 0
nomevelho = ''
soma_feminina = 0
for d in range(1, 5):
    print('==== {}ª PESSOA ===='.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    soma_idade += idade
    if d == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 21:
        soma_feminina += 1
media_grupo = soma_idade / 4
print('A média das idades do grupo vale {}'.format(media_grupo))
print('{} é o homem mais velho com {} anos'.format(nomevelho, maioridadehomem))
print('{} mulheres tem menos de 21 anos.'.format(soma_feminina))