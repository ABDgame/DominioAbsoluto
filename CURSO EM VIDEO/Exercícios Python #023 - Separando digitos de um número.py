# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados.
# Ex:
# Digite um número:1834
# unidade:4 dezena:3 centena:8 milhar:1
numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
