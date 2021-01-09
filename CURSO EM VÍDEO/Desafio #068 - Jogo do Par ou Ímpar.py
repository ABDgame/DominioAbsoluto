''' 
     Faça um programa que jogue par ou impar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.
'''
from  random import randint

while True:
     jogador = int(input('Diga um valor: '))
     computador = randint (0,10)
     total = jogador + computador
     tipo = ' '
     while tipo not in 'PI':
         tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
     print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')