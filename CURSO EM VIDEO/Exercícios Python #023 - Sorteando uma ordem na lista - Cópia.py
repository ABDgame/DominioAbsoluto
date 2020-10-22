# Desafio 020 - Sorteando uma ordem na lista
from random import sample
n1 = (input('Primeiro aluno:  '))
n2 = (input('Segundo  aluno: '))
n3 = (input('Terceiro aluno:  '))
n4 = (input('Quarto aluno: '))
sorteio = sample([n1, n2, n3, n4],k=4)
print('A ordem das apresentações é: \n{}'.format(sorteio))
