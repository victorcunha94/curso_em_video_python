valor = float(input('Qual o preço do produto? '))
print( '''========= Loja =========
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
op = int(input('Digite sua opção: '))
if op == 1:
    print('O valor a ser cobrado é R${:.2f} '.format(valor*0.90))
elif op == 2:
    print('O valor a ser cobrado é R${:.2f}'.format(valor*0.95))
elif op == 3:
    print('O valor a ser cobrado é R${:.2f}'.format(valor*1.2))
elif op == 4:
    total = (valor*1.2)
    totalparc = int(input('Em quantas parcelas você quer dividir? '))
    parcelas = total / totalparc
    print(' Sua compra será parcelada em {}x no valor de R${:.2f}'.format(totalparc, parcelas))
