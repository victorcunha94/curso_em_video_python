a = float(input('Lado a do triângulo: '))
b = float(input('Lado b do triângulo: '))
c = float(input('Lado c do trinâgulo: '))
if abs(a - b) < c < (a + b) and abs(b - c) < a < (b + c) and abs(a - c) < c < a + c:
    triangulo = True
    print('É triângulo.')
if triangulo is True and a == b == c:
    print('É um triângulo EQUILÁTERO')
if triangulo is True and (a == b != c or a == c != b or b == c != a):
    print('É um triângulo ISÓSCELES')
if triangulo is True and (a != b != c) and (a != c):
    print('É um triângulo ESCALENO')
