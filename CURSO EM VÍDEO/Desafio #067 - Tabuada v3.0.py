'''
    Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
'''
while True:
    número = int(input('Quer ver a tabuada de qual valor? '))
    print('~' * 40)
    if número < 0:
        break
    for calcular in range(1,11):
        print(f'{número} x {calcular} = {número*calcular}')
    print('~' * 40)
print('GAME OVER')