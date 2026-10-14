exp = str(input('\033[0;34mDigite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('\033[1;32mSua expressão é válida')
else:
    print('\033[1;31mSua expressão é inválida')
