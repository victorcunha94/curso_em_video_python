p1 = int(input('Quantos dias o carro passou alugado? '))
p2 = float(input('Quantos KM o carro rodou durante este tempo? '))
pagar = (p1*60)+(p2*0.15)

print('Como o carro ficou alugado por {} dias e rodou {:2}KM, você pagará R${}'.format(p1, p2, pagar) )