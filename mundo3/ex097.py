# Fazer o print
def escreva(msg):
    print('\033[1;33m~' * (len(msg) + 4))
    print(f'\033[1;35m  {msg}')
    print('\033[1;33m~' * (len(msg) + 4))


escreva('Teste 1')
escreva('Zé')
