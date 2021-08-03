a = float(input('Lado a do triângulo: '))
b = float(input('Lado b do triângulo: '))
c = float(input('Lado c do trinângulo: '))
if abs(a - b) < c < (a + b) and abs(b - c) < a < (b + c) and abs(a - c) < c < a + c:
    print('É triangulo.')
else:
    print('Não é triângulo.')
