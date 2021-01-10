'''
    Desafio #071
    Crie um programa que simule o funcionamento 
de um caixa eletrônico.
    No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o
programa vai informar quantas
células de cada valor serão entregues
    
    OBS: Considere que o caixa
possui cédulas de:
       R$50, 
       R$20, 
       R$10,00 
       e R$5,00   
    
'''
print('='*40)
print('         BANCO HORA DO SUFOCO   ')
print('='*40)
valor = int(input(' Valor Do Saque = R$ '))
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor%= 20
nota10 = valor // 10
valor%= 10
nota5 = valor // 5
print(f'notas de 50 = {nota50}')
print(f'notas de 20 = {nota20}')
print(f'notas de 10 = {nota10}')
print(f'notas de 5 = {nota5}')

        
    
     


