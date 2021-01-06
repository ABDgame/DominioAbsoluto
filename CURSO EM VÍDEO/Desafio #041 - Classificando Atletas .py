''' 
    Desafio #041 - Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
'''
print('-='*20)
print('        Confederação Nacional de Natação  ')
print('-='*20)
while True:
    from datetime import date
    atual = date.today().year
    nascimento = int(input('Ano de Nascimento: '))
    idade = atual - nascimento 
    print('O atleta tem {} anos. '.format(idade))
    if idade <= 9:
        print('Classificação: MIRIM')
    elif idade <= 14:
        print('Classificação: INFANTIL')
    elif idade <= 19:
        print ('Classificação: JÚNIOR ')
    elif idade <= 25:
        print (' Classificação: SÊNIOR ')
    else:
        print (' Classificação: MASTER')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Classificar Outro Atleta ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('-='*20)
print('         Pausa Para O Café ')
print('-='*20)