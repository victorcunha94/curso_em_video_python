número = 1
média = soma = cont = maior = menor = 0
mais = 's'
while mais == 's':
    while número != 0:
            número = int(input('Digite um número: '))
            mais = str(input('Quer continuar a digitar? [S/N] '))
            if número != 0:
                cont += 1
                soma += número
                média = (soma / cont)
            if cont == 1:
                maior = menor = número
            else:
                if número > maior:
                    maior = número
                if número < menor:
                    menor = número
            if mais != 's':
                 print('A média até o momento é {:.2f}, o maior número é {} e o menor {}.'.format(média, maior, menor))
