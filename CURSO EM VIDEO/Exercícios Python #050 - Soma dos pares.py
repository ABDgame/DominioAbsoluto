# Desafio 050 - Desenvolva um programa que leia
# seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado
# for apenas impar, desconsidere.
soma = 0
cont = 0
for contador in range(1,7):
    num = int(input('Digite o {} valor: '.format(contador))) 
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
