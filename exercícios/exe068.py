import random as rd
import time as tm
cont = 0
while True:
    paridade = str(input('Ímpar[i] ou Par[p]? ')).lower()
    humano = int(input('Digite um número de 1 a 5: '))
    computador = rd.randint(1, 6)
    s = humano + computador
    if 'i' in paridade and s % 2 != 0:
        print(f'o computador escolheu {computador} a soma vale {s}')
        print('Você Venceu.')
        cont += 1
    if 'p' in paridade and s % 2 == 0:
        print(f'o computador escolheu {computador} a soma vale {s}')
        print('Você Venceu.')
        cont += 1
    if 'p' in paridade and s % 2 != 0:
        print(f'o computador escolheu {computador} a soma vale {s}')
        print(f'Você Perdeu! mas venceu {cont} vezes.')
        break
    if 'i' in paridade and s % 2 == 0:
        print(f'o computador escolheu {computador} a soma vale {s}')
        print(f'Você Perdeu! mas venceu {cont} vezes.')
        break


