# Importações
from datetime import datetime


# Função
def voto(a):
    global i
    if i < 16:
        v = '\033[1;31mNão vota'
    elif 16 <= i <= 17 or i > 65:
        v = '\033[1;33mVoto opcional'
    elif 18 <= i <= 65:
        v = '\033[1;32mVoto obrigatório'
    return v
    return i


# Programa principal
print('\033[1;33m-' * 30)
while True:
    try:
        ano = int(input('\033[0;34mAno de nascimento: '))
        break
    except ValueError:
        print('\033[1;31mValor inválido. Tente novamente.')
i = datetime.today().year - ano
print(f'\033[1;34mCom {i} anos: {voto(ano)}.')
