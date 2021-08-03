print('===SEQUÊNCIA DE FIBONACCI==')
número_termos = int(input('Número de termos: '))
total = 4
primeiro_termo = 0
segundo_termo = 1
terceiro_termo = primeiro_termo + segundo_termo
print('0 - 1 - 1 - ', end='')
while total <= número_termos:
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    terceiro_termo = primeiro_termo + segundo_termo
    print('{}'.format(terceiro_termo), end=' - ')
    total +=1
print('FIM')
