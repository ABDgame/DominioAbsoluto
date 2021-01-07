'''   
    Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de 
uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
print('-='*20)
print('        Razão de uma PA')
print('-='*20)
while True:
    primeiro = int(input(' Primeiro termo: '))
    razão = int(input(' Razão: '))
    décimo = primeiro + (10 - 1) * razão 
    for contador in range(primeiro, décimo + razão, razão):
        print ('{}'.format(contador), end=' -> ')
        sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outra Razão de uma PA  ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)