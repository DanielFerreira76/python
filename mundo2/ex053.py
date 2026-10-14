f = str(input('\033[0;34mQual a frase? ').upper().strip())
if f == f[::-1]:
    print('\033[1;32mA frase é um palíndromo')
else:
    print('\033[1;31mA frase não é um palíndromo')
