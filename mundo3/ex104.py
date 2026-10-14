# Código escrito por amor.
# Por ela. Pela nossa vida. Pelo futuro

# Funções
def leiaint():
    while True:
        try:
            a = int(input('\033[0;34mDigite um número: '))
            break
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.')
    return a


# Programa Principal
print('\033[1;33m-' * 10)
n = leiaint()
print(f'\033[1;32mVocê acabou de digitar o número {n}.')
