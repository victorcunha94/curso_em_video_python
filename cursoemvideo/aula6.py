n = input('Digite aqui alguma coisa:  ')
print('A classe do que você digitou é ', type(n))
print('O que você digitou é numérico?', n.isalnum())
print('O que você digitou é alfanumérico?', n.isalpha())
print('O que você digitou está em capslock? ', n.isupper())
print('O que você digitou está em letra minúscula? ', n.islower())
print('É capitalizado? {}'.format(n.istitle()))


