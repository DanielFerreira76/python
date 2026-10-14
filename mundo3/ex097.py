# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro.

# Fazer o print
def escreva(msg):
    print('\033[1;33m~' * (len(msg) + 4))
    print(f'\033[1;35m  {msg}')
    print('\033[1;33m~' * (len(msg) + 4))


escreva('Teste 1')
escreva('Zé')
escreva('Eu amo a Lorena')
