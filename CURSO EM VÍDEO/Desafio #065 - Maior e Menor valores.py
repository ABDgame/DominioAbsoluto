'''
    Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar e digitar valores.
'''
resposta = 'S'
soma = 0
quantidade =0
média = 0
maior = 0
menor = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma += número 
    quantidade += 1
    if quantidade == 1:
        maior = menor = número 
    else:
        if número > maior:
            maior = número 
        if número < menor:
            nenor = número
    resposta = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
média = soma / quantidade
print('Você digitou {} números e a média foi {}'.format(quantidade, média))
print('O maior valor foi {}'.format(maior, menor))
