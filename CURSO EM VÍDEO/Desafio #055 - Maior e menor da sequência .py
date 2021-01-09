'''
  Desafio 055 - Faça um programa que leia
o peso de cinco pessoas. No final, mostre
qual foi a maior e menor peso lidos.
'''
print('::'*20)
print('        Analisador De Pesos  ')
print('::'*20)
while True:
    maior = 0
    menor = 0
    for p in range (1, 6):
        peso = float (input ( ' Peso do {} ° cidadão  :  '.format(p  )))
        if p == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print('O maior peso lido foi de {}kg'.format(maior))
    print('O menor peso lido foi de {}kg'.format(menor))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outros Pesos, Cidadão ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)
            
