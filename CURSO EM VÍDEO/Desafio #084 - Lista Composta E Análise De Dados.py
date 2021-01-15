'''
     Faça um programa que leia nome
e peso de vários cidadões, guardando
tudo em uma lista, No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
'''
# Início do break 
temporária = []
principal = []
maior = menor = 0
while True:
    temporária.append(str(input(' Nome:')))
    temporária.append(float(input(' Peso: ')))
    if len(principal) == 0:
        maior = menor = temporária[1]
    else:
        if temporária[1] > maior:
            maior = temporária[1]
        if temporária[1] < menor:
            menor = temporária[1] 
    principal.append(temporária[:])
    temporária.clear()


#final do while, início do break    
    resposta = str(input(' Quer Continuar [S/N]'))
    if resposta in 'Nn':
        break
print('-='*20)        
print(f'Ao todo, você cadastrou {len(principal)} cidadões.')
print(f'O Maior Peso foi de {maior}kg. Pertece à ', end='')
for peso in principal:
    if peso[1] == maior:
        print(f'{peso[0]} ',end='')
print()
print(f'O Menor Peso foi de {menor}kg. Pertence à ', end='')
for peso in principal:
    if peso[1] == menor:
        print(f'{peso[0]} ', end='')
print('_='*20)
print('        Pausa Para O Café ')
print('_='*20)

