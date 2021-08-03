from random import randint
n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior = n[0]
if n[1] > n[0]:
    maior = n[1]
if n[2] > maior:
    maior = n[2]
if n[3] > maior:
    maior = n[3]
if n[4] > maior:
    maior = n[4]
menor = n[0]
if n[1] < menor:
    menor = n[1]
if n[2] < menor:
    menor = n[2]
if n[3] < menor:
    menor = n[3]
if n[4] < menor:
    menor = n[4]
print(n)
print(f'O maior valor da tupla é {maior}')
print(f'O menor valor da tupla é {menor}')