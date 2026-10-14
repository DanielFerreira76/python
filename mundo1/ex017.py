from math import hypot

c1 = float(input('Valor do primeiro cateto: '))
c2 = float(input('Valor do segundo cateto: '))
h = hypot(c1, c2)
print('O valor da hipotenusa é: {:.2f}.'.format(h))
