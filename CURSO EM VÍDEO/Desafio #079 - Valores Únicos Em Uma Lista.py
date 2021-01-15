'''
    Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados: em ordem crescente.
'''
números = list() 
while True:
    número = int(input('Digite um valor: '))
    if número not in números:
        números.append(número)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer Continuar? [S/N]' ))
    if resposta in 'Nn':
        break
print('::'*30)
números.sort()
print(f'Você digitou os valores {números}')
