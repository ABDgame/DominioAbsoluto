'''
 Desafio 015 - 
'''
while True:
    dias = int(input('Quantos dias alugados? '))
    km = float(input('Quantos quilômetros rodados? '))
    pago = (dias * 60) + (km * 0.15)
    print('O total a pagar é de R${:.2f}'.format(pago))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular outros dias ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')