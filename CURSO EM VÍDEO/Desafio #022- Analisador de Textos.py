'''
   Crie um programa que leia o nome completo de uma pessoa e
mostre:
   O nome com todas as letras maiúsculas e minúsculas.
   Quantas letras ao todo (sem considerar espaços).
   Quantas letras tem o primeiro nome.
'''
while True:
    nome = str(input('Digite um nome completo: ')).strip() 
    print('Analisando o nome...')
    print('O nome em maiúscula é {}'.format(nome.upper()))
    print('O nome em minúscula é {}'.format(nome.lower()))
    print('O nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
    print ('O primeiro nome tem {} letras'.format(nome.find(' ')))
    separa = nome.split()
    print('O primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Analisar outro nome ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')