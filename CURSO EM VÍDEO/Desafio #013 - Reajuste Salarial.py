'''
 Desafio 013 -
'''
while True:
    colaborador = str(input('Nome do colaborador: '))
    salário = float(input('Qual é o salário  atual do funcionário? R$'))
    aumento = salário + (salário * 37/ 100)
    print(' O salário do(a) colaborador(a) {},que era R${}, com o aumento  de  37% será  R${}'.format(colaborador,salário,aumento))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Outro Reajuste Salarial ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')    