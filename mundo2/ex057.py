s = input('\033[0;34mInforme o seu sexo: [M/F]')[0].upper()
while s not in 'MF':
    s = input('\033[1;31mDados inválidos, informe o seu sexo: [M/F]')[0].upper()
if s == 'M':
    print('\033[1;32mSexo masculino registrado com sucesso')
elif s == 'F':
    print('\033[1;32mSexo feminino registrado com sucesso')
