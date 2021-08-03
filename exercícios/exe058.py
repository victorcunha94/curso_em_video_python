from random import randint
computador = randint(1, 10)
jogador = ''
cont = 0
while computador != jogador:
    jogador = int(input('Digite um número: '))
    if computador == jogador:
        print('Você venceu.')
    else:
        cont += 1
        print('Você perdeu.')
print('Você precisou de {} tentativas para acertar o número.'.format(cont))
print('FIM')