'''
    Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles(desconsiderando o flag 999).
'''
número = 0
contador = 0
soma = 0
número = int(input('Digite um número inteiro [999 para cancelar]: '))
while número != 999:
    soma += número
    contador += 1
    número = int(input('Digite um número inteiro [999 para cancelar]: '))
print('Você digitou {} números e a soma entre eles foi {}. '.format(contador, soma))
