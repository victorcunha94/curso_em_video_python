n = 1
impar = par = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} ímpares.'.format(par, impar))
print('FIM')