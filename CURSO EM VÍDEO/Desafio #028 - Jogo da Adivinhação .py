'''
    Desafio 028 - Jogo da Adivinhação v. 1.0
'''
while True:
    import random
    pc = random.randint(0,5)
    vc = int(input('Digite um número de 0 a 5:'))
    if pc==vc:
        print('Você ganhou!!!')
    else:
        print('O PC ganhou!!!')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Digitar outro número de 0 a 5: ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')
