'''  
 Desafio 052 - Faça um programa que leia um
número inteiro e diga se ele é ou não 
um número primo.
'''
while True:
    num = int(input('Digite um número: '))
    total = 0
    for contador in range(1, num + 1):
        if num % contador == 0:
            print('\033[33m', end='')
            total += 1
        else:
            print('\033[31m' , end='')
        print('{} '.format(contador), end='')
    print ('O número {} foi divisível {} vezes'.format(num, total))
    if total == 2:
        print ('E por isso ele É PRIMO!')
    else:
        print (' E por isso ele NÃO É PRIMO!')
    sair = ' '
    while sair not in 'SN':
        sair = str(input(' Digitar Outro Número  ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)