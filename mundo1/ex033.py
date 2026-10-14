n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
ma = n1
me = n1
if n2 > ma and n2 > n3:
    ma = n2
if n2 < me and n2 < n3:
    me = n2
if n3 > ma and n3 > n2:
    ma = n3
if n3 < me and n3 < n2:
    me = n3
print('O maior valor foi: {}.'.format(ma))
print('O menor valor foi: {}.'.format(me))
