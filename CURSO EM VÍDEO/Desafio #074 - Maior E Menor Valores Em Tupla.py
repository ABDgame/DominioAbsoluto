'''
    Crie um programa que vai gerar cinco números aleatórios e
colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor valor que
estão na tupla.
'''
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print (f'Os valores sorteados foram:', end=' ')
for número in números:
     print(f'{número}', end=' ')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
        
