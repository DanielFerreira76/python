s1 = float(input('\033[0;34mPrimeiro Segmento: '))
s2 = float(input('\033[34mSegundo Segmento: '))
s3 = float(input('\033[34mTerceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('\033[1;32mOs segmentos podem formar um triângulo equilátero.')
    elif s1 != s2 != s3 != s1:
        print('\033[1;32mOs segmentos podem formar um triângulo escaleno.')
    else:
        print('\033[1;32mOs segmentos podem formar um triângulo isósceles.')
else:
    print('\033[1;31mOs segmentos não podem formar um triângulo.')
