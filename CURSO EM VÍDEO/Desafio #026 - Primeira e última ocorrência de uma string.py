'''
    Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
'''
while True:
    frase = str(input('Digite uma frase: ')).upper().strip()
    print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
    print('A primeira letra "A" aparece na posição  {}.'.format(frase.find('A')+1))
    print('A última letra "A" aparece na posição {}.'.format(frase.rfind('A')))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outra Frase ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')