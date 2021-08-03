import random
aluno1 = str(input('Digite aqui o nome do primeiro aluno: '))
aluno2 = str(input('Digite aqui o nome do segundo aluno: '))
aluno3 = str(input('Digite aqui o nome do terceiro aluno: '))
esc = random.choices([aluno1, aluno2, aluno3])
print('O aluno sorteado foi {}'.format(esc))
print(esc, esc, esc)