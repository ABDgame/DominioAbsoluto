''' 
    Desafio #038 - Comparando números
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela um mensagem:
  - O Primeiro valor é maior
  - O segundo valor é maior 
  - Não existe valor maior. Os dois valores são iguais.
'''
print('-='*20)
print('        Comparando Números')
print('-='*20)
while True:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    if n1 > n2:
        print ('O primeiro valor é maior')
    elif n2 > n1:
        print ('O segundo valor é menor')
    elif n1 == n2:
        print ('Os dois valores são iguais ')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Reajuste Salarial ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)