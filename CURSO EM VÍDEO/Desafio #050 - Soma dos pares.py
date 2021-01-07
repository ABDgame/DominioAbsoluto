''' 
 Desafio 050 - Desenvolva um programa que leia
seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado
for apenas impar, desconsidere.
'''
print('::'*20)  
print('        Somar Apenas Os Pares!!!')  
print('::'*20)
while True:
    soma = 0
    cont = 0
    for contador in range(1,7):
        num = int(input('Digite o {} valor: '.format(contador)))
        if num % 2 == 0:
            soma += num
            cont += 1
    print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Somar Outra Sequência De Pares ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)  
print('        Pausa Para O Café!!!')  
print('::'*20)  
    
