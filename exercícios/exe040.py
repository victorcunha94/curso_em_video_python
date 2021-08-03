nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota '))
media = (nota1 + nota2)/2
print('A Média é {}. Portanto'.format(media))
if media < 5:
    print('O aluno está REPROVADO.')
elif media == 5 or media <= 6.9:
    print('O aluno vai para a RECUPERAÇÂO')
elif media >= 7:
    print('O aluno está APROVADO.')
