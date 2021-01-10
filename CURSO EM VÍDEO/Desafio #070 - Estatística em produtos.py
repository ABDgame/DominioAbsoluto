'''
     Desafio #070
     Crie um programa que leia o nome e o
preço de vários produtores. O programa 
deverá perguntar se o usuário vai
continuar. No final, mostre:
    - Qual é o total gasto no conpra.
    - Quantos produtos custam mais de R$ 1000.
    - Qual é o nome do produto mais barato.
'''
total = totalmil = menorpreço = contador = 0
produtobarato = ''
print('-='*20)
print('        LOJA TRECHOS DE CÓDIGO')
print('-='*20)
while True:
    produto = str(input('Nome do Produro: '))
    preço = float(input('Preço: R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        totalmil += 1 
    if contador == 1 or preço < menorpreço:
        menorpreço = preço
        produtobarato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input(' Quer Continuar? [S/N]   ')).strip( ).upper( )[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('  FIM DO PROGRAMA   '))
print(f' Total da compra R${total:.2f}')
print(f'{totalmil} produto(s)  valendo MAIS de R$ 1000,00')
print (f' Produto mais barato é o(a) {produtobarato} no valor de  R${menorpreço:.2f}')
print('::'*20)
print('        Pausa Para O Café ')  
print('::'*20) 
        



