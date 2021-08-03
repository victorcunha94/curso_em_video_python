from random import choice
print('=-='*20)
print('Lute contra o computador no Jokenpô')
print('=-='*20)
comp = choice(['PEDRA', 'PAPEL', 'TESOURA'])
usu = str(input('Pedra, papel ou tesoura? digite um dos três: ')).upper().strip()
if usu == comp:
    print('Deu igual, jogue novamente:')
elif usu == 'PEDRA' and comp == 'PAPEL':
    print('O computador venceu.')
elif usu == 'PEDRA' and comp == 'TESOURA':
    print('Você venceu, parabéns!')
elif usu == 'PAPEL' and comp == 'PEDRA':
    print('Você venceu, parabéns!')
elif usu == 'PAPEL' and comp == 'TESOURA':
    print('O computador venceu.')
elif usu == 'TESOURA' and comp == 'PAPEL':
    print('Você venceu, parabéns!')
elif usu == 'TESOURA' and comp == 'PEDRA':
    print('O computador venceu.')
print('O computador escolheu {}'.format(comp))
