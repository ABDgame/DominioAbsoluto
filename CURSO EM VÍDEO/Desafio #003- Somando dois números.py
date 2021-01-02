'''
    Desafio 003 - Crie um programa que leia dois números e
mostre a soma entre eles.
'''
while True:
    n1 = int (input ('Digite um valor: '))
    n2 = int (input ('Digite outro valor: '))
    s = n1 + n2
    print('A soma entre {} e {} é igual a {} ! '.format (n1,n2,s))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Hora Do Recreio!!!')    

