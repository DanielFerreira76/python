n1 = int(input('\033[0;34mPrimeiro número: '))
n2 = int(input('\033[34mSegundo número: '))
if n1 > n2:
    print('\033[1;32mO primeiro número é o maior')
elif n1 < n2:
    print('\033[1;32mO segundo número é o maior')
elif n1 == n2:
    print('\033[33mAmbos os números são iguais')
