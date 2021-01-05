'''  
    Desafio #039 - Alistamento Militar 
Faça um programa que leia o ano de nascimento de um jovem e informe,
se é a hora de se alistar ou se já passou do tempi do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
'''
print('-='*20)
print('        Alistamento Militar')
print('-='*20)
while True:
    from datetime import date
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem  nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print ('Você tem se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade 
        print ('Ainda faltam {} anos para o alistamento '.format (saldo))
        ano = atual + saldo
        print ('Seu alistamento será  em {}, bebê!'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print ('Seu alistamento foi em {}'.format(ano))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Reajuste Salarial ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('       Pausa Para O Café  ')
print('::'*20)