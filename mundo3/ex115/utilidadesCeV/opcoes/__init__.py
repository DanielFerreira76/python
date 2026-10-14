def mostrar():
    import os

    print('\033[1;32m', end='')
    arquivo = 'pessoas.txt'
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r', encoding="utf-8") as arq:
                for c in arq:
                    dado = c.split(';')
                    dado[1] = dado[1].replace('\n', '')
                    print(f'\033[1;32m{dado[0]:<30}\033[1;34m{dado[1]:<2} anos')
        except:
            print('\033[1;31mHouve um erro ao abrir o arquivo')
    else:
        try:
            with open(arquivo, 'w', encoding="utf-8") as arq:
                print(f'\033[1;32mO arquivo {arquivo} não existia e foi criado.')
        except:
            print('\033[1;31mHouve um erro ao criar o arquivo')


def cadastrar(arquivo, a='desconhecido', b=0):
    try:
        c = open(arquivo, 'at')
    except:
        print('\033[1;31mHouve um erro ao abrir o arquivo')
    else:
        try:
            c.write(f'\n{a};{b}\n')
        except:
            print('\033[1;31mHouve um erro ao cadastrar a pessoa no arquivo')
        else:
            print(f'\033[1;32mCadastro de {a} realizado com sucesso!')
        finally:
            c.close()

