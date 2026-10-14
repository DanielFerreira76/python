# Funções
def notas(*a, sit=False):
    '''
    Mostra a situação de um aluno de acordo com suas notas.
    :param a: Notas do aluno
    :param sit: Situação do aluno
    :return: Boletim do aluno
    '''
    ma = e = 0
    for b in a:
        if b > ma:
            ma = b
        me = ma
        if b < me:
            me = b
    for d in a:
        e += d
    m = e / len(a)
    if sit == True:
        if m < 5:
            s = 'ruim'
        elif m < 7:
            s = 'razoável'
        else:
            s = 'boa'
        c = {'total': len(a), 'maior': ma, 'menor': me, 'média': m, 'situação': s}

    else:
        c = {'total': len(a), 'maior': ma, 'menor': me, 'média': m}
    return c


# Programa Principal
print(notas(5.6, 9, 7.8, 1, sit=True))
print(notas(4, 4, 6, 0, 8.192837))
help(notas)
