'''
    Desafio #088 - Palpites Para A MEGA SENA a criar 
palpites. O programa vai perguntar quantos jogos serão 
gerados e vai sortear 6 números entre 1 e 60 para cada
e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.    
    
'''
from random import randint
lista = list()
jogos = list()
print('-' * 40)
print('          JOGO DA MEGA SENA')
print('-' * 40)
quantidade = int(input('Quantos Jogos Você Quer Que Eu Sorte?'))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        número = randint(1, 60)
        if número not in lista:
            lista.append(número)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1         
print('-='* 3, f'   SORTEANDO {quantidade} JOGOS', '-=' * 3)
for índice, lista in enumerate(jogos):
    print(f' Jogo {índice+1}: {lista}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
    
    
