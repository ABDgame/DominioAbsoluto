'''
    Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou IMPAR.
'''
while True:
    numero = int(input('Digite um número qualquer: '))
    resultado = numero % 2
    if resultado == 0:
        print ('O número {} é PAR'.format(numero))
    else:
        print ('O número {} é IMPAR'.format(numero))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outro Número ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')
    