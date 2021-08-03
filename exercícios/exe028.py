from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input('Eu pensei em um número de 0 a 5. Tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns você me venceu!!!')
else:
    print('Ganhei, pensei no número {} e não em {}'.format(computador, jogador))
