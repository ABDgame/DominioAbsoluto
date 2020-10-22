# Desafio 054 - Crie um programa que leia o ano de
# nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano a pessoa? '))
idade = atual - nasc
if idade >= 18:
    print('Essa pessoa é maior')
else:
    print('Essa pessoa é menor')