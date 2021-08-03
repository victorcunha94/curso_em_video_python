import math
catadj = float(input('Digite aqui o catéto adjacente do triângulo: '))
catopo = float(input('Digite aqui o cateto oposto do triângulo: '))
rep = pow(catadj, 2) + pow(catopo, 2)
print('A hipotenusa do triângulo cujos catetos valem {} e {} é igual a {}'.format(catopo, catadj, rep))