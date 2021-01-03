'''
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem
que ele foi multado.
    A multa vai custar R$7,00 por  cada Km acima do limite.
'''
while True:
    velocidade = float(input ('Qual a velocidade atual do carro?  '))
    if velocidade > 80:
        print ('Multado(a)!')
        multa = (velocidade - 80) * 7
        print('Você irá pagar uma multa de R${:.2f} !'.format(multa))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outras Velocidades ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')

