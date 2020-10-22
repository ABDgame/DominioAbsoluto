# Desafio 019
from random import choice
print('Digite os doces para sorteio')
n1 = (input('Primeiro doce:  '))
n2 = (input('Segundo  doce: '))
n3 = (input('Terceiro doce:  '))
n4 = (input('Quarto doce: '))
lista = n1, n2, n3, n4
print('O doce escolhido foi: {} '.format(choice(lista)))