# Desafio - 047 Crie um programa que mostre na
# tela todos os números pares que
# estão no intervalo entre 1 e 50.
from time import sleep
for n in range(2,51,2):
    print(n, end=' ')
    sleep(0.5)
print('Acabou')