while True:
    nome = str(input('Digite um nome completo: ')).strip( )
    nome = nome.split()
    print('O primeiro nome é {}'.format(nome[0]))
    print('O último nome é {}'.format(nome[len(nome)-1]))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outro Nome Completo ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')