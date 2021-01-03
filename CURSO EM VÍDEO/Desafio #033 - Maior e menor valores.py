'''  
  Desafio 033 - Faça um programa que leia três 
números e mostre qual é o maior e qual é o menor
'''
while True:
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    c = int(input('Terceiro valor: '))
# Verificando quem é o menor 
    menor = a
    if  b  <  a  and  b  <  c:
        menor = b
    if  c  <  a and  c  <  b:
        menor = c
# Verificando quem é o maior
    maior  = a
    if  b  >  a and b > c:
        menor = b
    if  c >  a and  c  >  b:
        maior = c
    print ('O menor valor digitado foi {} '.format(menor))
    print ('O maior valor digitado foi {} '.format(maior))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Comparar Outros Valores  ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')