'''
   Faça um programa que leia o comprimento do 
cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o
comprimento da hipotenusa.
'''
while True:
    from math import hypot
    oposto = float(input('Comprimento do cateto oposto: ')) 
    adjacente  = float(input('Comprimento do cateto adjacente: ')) 
    hipotenusa = hypot(oposto, adjacente)
    print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outros Comprimentos ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')
