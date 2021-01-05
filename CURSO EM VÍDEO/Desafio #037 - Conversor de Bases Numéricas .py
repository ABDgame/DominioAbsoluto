'''
    Desafio 037 
Escreva um programa que leia um número inteiro qualquer 
e peça para o usuário escolher qual será 
a base de conversão:
''' 
print('-='*20)        
print('        Base De Conversão !!!') 
print('-='*20)
while True:
    num = int(input('Digite um número inteiro qualquer  '))
    print(''' Escolha uma das bases para conversão:
    [ 1 ] Binário 
    [ 2 ] Octal
    [ 3 ] Hexadecimal ''')
    opção = int(input('Sua opção: '))
    if opção == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
    elif opção == 2:
        print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
    elif opção  == 3:
        print('{} convertido para HEXADECIMAL  é igual a {}'.format(num, hex(num)[2:])) 
    else:
        print('Opção inválida. Tente novamente.')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Número Inteiro? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)        
print('        Pausa Para O Café !!!') 
print('::'*20)          

