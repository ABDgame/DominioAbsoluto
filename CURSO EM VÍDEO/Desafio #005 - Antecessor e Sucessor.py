''' 
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
'''
while True:
    valor = int(input('Digite um número: ')) 
    print('Analisando o número {}, seu antecessor é {} e o seu sucessor é {}'.format(valor,(valor-1),(valor+1))) 
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Digitar Outro Número ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')




