'''
    Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de descontos.
'''
while True:
    #cliente = str(input('Qual é seu nome? ')
    #produto = str(input('Qual o nome do seu produto? '))  
    preço = float(input('Quanto é o preço do seu produto? R$'))
    novo = preço - (preço * 5/ 100)
    print('O(A) { } que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, preço, novo))
    