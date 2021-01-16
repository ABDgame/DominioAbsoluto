'''
    Crie um programa onde o usuário possa digitar sete valores 
númericos e cadastre-os em uma lista única que mantenha 
srparados os valores pares e impares. No final, mostre os
valores pares e impares em ordem crescente.
'''
número = [[], []]
valor = 0
for contador in range(1,8):
    valor = int(input(f'Digite {contador}° valor: '))
    if valor % 2 == 0:
        número[0].append(valor)
    else:
        número[1].append(valor)
print('-=' *20)
número[0].sort()
número[1].sort()
print(f'Valores PARES digitados foram: {número[0]}')
print(f'Valores ÍMPARES digitados foram: {número[1]}')
print('::'*20)
print('       Pausa Para O Café ')
print('::'*20)
