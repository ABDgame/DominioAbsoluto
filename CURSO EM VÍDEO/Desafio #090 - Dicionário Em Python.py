'''
     Faça um programa que leia nome e média de
um aluno, guardando também a situação 
em um dicionário. No final, mostre o
conteúdo da estrutura na tela.
    
'''
aluno = dict()
while True:
    aluno['nome'] = str(input('Nome: '))
    aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['média'] >= 7:
        aluno['situação'] = 'APROVADO'
    elif 5 <= aluno['média'] < 7:
        aluno['situação'] = 'RECUPERAÇÃO'
    else:
        aluno['situação'] = 'REPROVADO'
    for chave, valor in aluno.items( ):
        print(f'  - {chave} é igual a {valor}')
    resposta = str(input('Quer Avaliar Outro Aluno? [S/N]'))
    if resposta in 'Nn':
        break
print('-='*20)
print('       Pausa Para O Café ')
print('-='*20)
