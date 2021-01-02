'''
    Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na
tela a sua tabuada. 
'''
while True:
    num = int(input('Digite um número pra ver sua tabuada: '))
    print('☆' * 8)
    print('{} x {:2} = {}' .format(num, 1 , num*1))
    print('{} x {:2} = {}' .format(num, 2 , num*2))
    print('{} x {:2} = {}' .format(num, 3 , num*3))
    print('{} x {:2} = {}' .format(num, 4 , num*4))
    print('{} x {:2} = {}' .format(num, 5 , num*5))
    print('{} x {:2} = {}' .format(num, 6 , num*6))
    print('{} x {:2} = {}' .format(num, 7 , num*7))
    print('{} x {:2} = {}' .format(num, 8 , num*8))
    print('{} x {:2} = {}' .format(num, 9 , num*9))
    print('{} x {:2} = {}' .format(num, 10 , num*10))
    print('☆' * 8)
    sair = ' '
    while sair not in 'SN':
        sair = str(input(' Outra Tabuada ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    