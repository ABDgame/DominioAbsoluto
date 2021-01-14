'''
    Faça um programa que leia 5 valores numéricos e guarde-os em
uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
'''
listanúmero = []
maior = 0
menor = 0
for contador in range(0,5):
    listanúmero.append(int(input(f'Digite um valor para a Posição {contador}: ')))
    if contador == 0:
        maior = menor = listanúmero[contador]
    else:
        if listanúmero[contador] > maior:
            maior = listanúmero[contador]
        if listanúmero[contador] < menor:
            menor = listanúmero[contador]
print('='*40)
print(f'Você digitou os valores {listanúmero}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for i, valor in enumerate(listanúmero):
    if valor == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} na posição ', end=' ')
for i, valor in enumerate(listanúmero):
    if valor == menor:
        print(f'{i}...', end=' ')
print()
print('='*40)
    
     