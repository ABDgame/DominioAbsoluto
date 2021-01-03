'''
    Desafio 034 
Escreva um programa que pergunte o salário de um funcionário e calcule o #valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
print('::'*20)
print('          Reajuste Salarial     ')
print('::'*20)
while True:
    salário = float(input('Qual é o salário do funcionário? R$ '))
    if salário <= 1250:
        novo = salário + (salário * 15/100)
    else:
        novo = salário + (salário * 10/100)
    print ('O salário era R${:.2f}, foi para R${:.2f} . '.format(salário, novo))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Reajuste Salarial ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('          Pausa Para O Café!!!    ')
print('::'*20)    