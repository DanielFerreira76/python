b = float(input('Largura: '))
h = float(input('Altura: '))
a = b * h
t = a / 2
print('A sua parede tem dimensão igual a {:.2f}m x {:.2f}m e a área de {:.2f}m².'.format(b, h, a))
print('Para pintar ela será necessário {:.2f} litros de tinta.'.format(t))
