'''
    Desafio 014 -
'''
while True:
    Celsius = float(input('Informe a temperatura em Celsius: '))
    Fahrenheit = ((9*Celsius)/5) + 32
    print ( 'A temperatura de {} Celsius corresponde a {} Fahrenheit'.format(Celsius, Fahrenheit))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Outra Temperatura em Celsius? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')