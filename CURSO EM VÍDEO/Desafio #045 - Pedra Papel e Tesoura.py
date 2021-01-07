'''
    Desafio 045
Crie um programa que faça o smartphone  jogar jokenpô
com você.
'''
print('-='*20)
print('        Jogo Jokenpô ')
print('-='*20)
while True:
    from random import randint 
    from time import sleep
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint (0, 2 )
    print ('''Suas operações:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input ('Qual é  a sua jogada? '))
    print ('JO')
    sleep(1)
    print ('KEN')
    sleep(1)
    print ('PO !!!')
    print('-=' * 14)
    print('O smartphone escolheu {}'.format(itens[computador] ))
    print ('Jogador jogou {}'.format(itens[jogador]))
    print ('-=' * 14)
    if computador == 0:
        if jogador == 0:
            print ('EMPATE')
        elif jogador == 1:
            print ('JOGADOR VENCE')
        elif jogador == 2:
            print ('SMARTPHONE  VENCE')
        else:
            print ('JOGADA INVÁLIDA!')
    elif computador == 1:
        if jogador == 0:
            print (' SMARTPHONE  VENCE ')
        elif jogador == 1:
            print ('EMPATE ')
        elif jogador == 2:
            print ('JOGADOR VENCE')
        else :
            print (' JOGADA INVÁLIDA! ')
    elif computador == 2:
        if jogador == 0:
            print ('JOGADOR VENCE')
    elif jogador == 1:
          print ('SMARTPHONE  VENCE')
    elif jogador == 2:
          print ('EMPATE')
    else :
          print (' JOGADA INVÁLIDA! ')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Jogar Jokenpô Novamente  ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)
    
        

