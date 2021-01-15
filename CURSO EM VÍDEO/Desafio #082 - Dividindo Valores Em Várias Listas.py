'''
    Desafio #082
    Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores impares dugitados,
respectivamente. Ao final, mostre o conteúdo das três listas
geradas. 
'''
número = list()
pares = list()
ímpares = list()
while True:
    número.append(int(input('Digite um número: ')))
    resposta = str(input('Quer Continuar? [S/N]'))
    if resposta in 'Nn':
        break
for impar, valor in enumerate(número):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        ímpares.append(valor)
print('-='*20)
print(f'A lista completa é {número}')
print(f'A lista de Pares é {pares}')
print(f'A lista de ímpares é {ímpares}')

