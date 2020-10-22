# Exercício  Python 038 - Comparando números
# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela um mensagem:
# - O Primeiro valor é maior
# - O segundo valor é maior 
# - Não existe valor maior. Os dois valores são iguais.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print ('O primeiro valor é maior')
elif n2 > n1:
    print ('O segundo valor é menor')
elif n1 == n2:
    print ('Os dois valores são iguais ')
