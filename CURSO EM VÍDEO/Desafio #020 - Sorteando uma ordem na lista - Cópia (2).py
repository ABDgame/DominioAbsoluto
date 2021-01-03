'''
    Desafio 020 - Sorteando uma ordem na lista
'''
while True:
    from random import sample
    n1 = (input('Primeiro aluno:  '))
    n2 = (input('Segundo  aluno: '))
    n3 = (input('Terceiro aluno:  '))
    n4 = (input('Quarto aluno: '))
    sorteio = sample([n1, n2, n3, n4],k=4)
    print('A ordem das apresentações é: \n{}'.format(sorteio))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Sortear outra sequência ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')
