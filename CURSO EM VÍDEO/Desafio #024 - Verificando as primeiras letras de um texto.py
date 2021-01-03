'''
    Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com a letra "BAURU".
'''
while True:
    cidade = str(input('Em que cidade você nasceu?')).strip()
    print(cidade[:8].upper()== 'BAURU')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outra Cidade ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')