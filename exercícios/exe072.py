nomes = 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Desenove', 'Vinte'
número = int(input('Digite um número de 0 a 20: '))
while número not in range(0, 21):
    número = int(input('Por favor, digite um número válido de 0 a 20: '))
    if número in range(0, 21):
        break
print(f'{nomes[número - 1]}, foi o número que você digitou. ')

