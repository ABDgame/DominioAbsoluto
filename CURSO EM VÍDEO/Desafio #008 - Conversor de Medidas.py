'''
    Escreva um programa que leia um valor em metros e o exiba
convertido em centimetros e milímetros.    
'''
while True:
    medida = float(input('Uma distância em Metros: '))
    cm = medida * 100
    mm = medida * 1000
    print('A medida de {}m corresponde a {}mm'.format(medida, cm, mm))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Converter Outra Distância  ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    
