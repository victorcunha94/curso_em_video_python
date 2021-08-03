print('Descubra o quadrante do ponto no plano!!')
x = float(input('Eixo das abcissas(x): '))
y = float(input('Eixo das ordenadas(y): '))
if x > 0 and y > 0:
    print('O ponto pertence ao quandrante 1 ')
elif x > 0 and y < 0:
    print('O ponto pertence ao quadrante 4')
elif x < 0 and y > 0:
    print('O ponto pertence ao quadrante 2')
else:
    print('O pronto pertence ao quadrante 3.')