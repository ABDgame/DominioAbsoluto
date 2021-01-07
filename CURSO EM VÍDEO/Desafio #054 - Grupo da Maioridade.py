'''  
    Desafio 054 - Crie um programa que leia o ano de
nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
'''
while True:
    from datetime import date
    atual = date.today().year
    totmaior = 0
    totmenor = 0
    for cidadão in range(1,8):
        nascimento  = int(input('Em que ano o {}° cidadão? '.format(cidadão)))
        idade = atual - nascimento 
        if idade >= 21:
            totmaior += 1
        else:
            totmenor += 1
    print('Ao todo tivemos {} cidadões maiores de idades'.format(totmaior))
    print('Ao todo tivemos {} cidadões menores de idades'.format(totmenor))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outros Anos De Nascimento ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)    