# Funções
def fatorial(a, show=False):
    """
    Retorna o fatorial de `a`. Se show for True, imprime o cálculo passo a passo.
    """
    if a < 0:
        raise ValueError("Não existe fatorial de número negativo.")
    if a == 0:
        if show:
            print(f'\033[1;32m0! = 1')
            print('\033[1;33m-=' * 15)
        return 1
    res = 1
    for i in range(a, 0, -1):
        res *= i
    if show:
        termos = [str(i) for i in range(a, 0, -1)]
        expr = ' \033[1;35m×\033[1;32m '.join(termos)
        print(f'\033[1;32m{expr} = {res}')
    else:
        print(f'\033[1;32m{a}! = {res}')
    print('\033[1;33m-=' * 15)
    return res

# Programa Principal
fatorial(5)
fatorial(9, show=True)
