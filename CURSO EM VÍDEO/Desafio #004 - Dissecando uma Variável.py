'''
   Faça um programa que leia algo pelo teclado e mostre na tela o seu 
tipo primitivo e todas as informações possíveis sobre ele.

'''
while True:
    valor = input('Digite algo: ')
    print(f'O tipo primitivo desse valor é ', type(valor))
    print(f'Só tem espaços? ', valor.isspace())
    print (f'É um número? ', valor.isnumeric())
    print (f'É alfabético? ', valor.isalpha())
    print (f'É alfanumérico? ', valor.isalnum())
    print (f'Está em maiúscula?', valor. isupper())
    print (f'Está em minúscula?', valor.islower())
    print (f'Está capitalizada?', valor.istitle())
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Digitar outra coisa ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Hora Do Recreio!!!')    
