'''
    Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens de até 200km e R$0,45 para viagens mais longas.
    
    if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
'''
while True:
    distancia = float(input('Qual a distância da sua viagem? '))
    print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
    preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular o preço de outra passagem? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')