pa = ('aprender', 'programar', 'linguagem', 'python',
      'curso', 'grátis', 'estudar', 'praticar',
      'trabalhar', 'mercado', 'programador', 'futuro')
for p in pa:
    print(f'\n\033[0;34mNa palavra {p.upper()} temos\033[1;32m', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
