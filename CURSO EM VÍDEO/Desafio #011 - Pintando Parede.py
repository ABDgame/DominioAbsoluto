'''
    Desafio 011 - Faça um programa que leia a largura e a altura de uma parade em
metros, calcule a sua área e a quantidade de tinta necessária de tinta necessária 
para pintá-los, sabendo que cada litro de tinta, pinta uma área de 2m.    
'''
while True:
    largura = float(input('Largura da Parede '))
    altura = float(input (' Altura da Parede '))
    área = largura * altura
    print('Sua parede tem a dimensão de {}x{} e sua área é de{}m2'.format(largura, altura, área))
    tinta = área / 2
    print ('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Outra Parede ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    