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
total = valor
nota = 50
totalnotas = 0
while True:
    if total >= nota:
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total De {totalnotas} notas de R${nota} ')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        totalnotas = 0
        if total == 0:
            break
print('::'*20)
print(         '        Agradecemos A Preferência    ')
print('::'*20)
        
    
     


