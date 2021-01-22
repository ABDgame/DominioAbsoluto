'''
     Crie um programa que leia nome,
gênero e idade de várias pessoas, 
guardando os dados de cada pessoa
em uma dicionário e todos os dicionários 
em uma lista. No final, mostre:
    
    A) Quantas pessoas cadastradas
    B) A média de idade.
    C) Uma lista com mulheres.
    D) Una lista com idade acima
    da média.
'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['gênero'] = str(input('Gênero: [M/F] ')).upper()[0]
        if pessoa['gênero'] in 'MF':
            break
        print('ERRO! Por gentileza, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for cidadão in galera:
    if cidadão['gênero'] in 'Ff':
        print(f'{cidadão["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for cidadão in galera:
    if cidadão['idade'] >= média:
        print('  ')
        for chave, valor in cidadão.items():
            print(f'{chave} = {valor}; ', end='') 
        print()
print('::'*20)
print('           Pausa Para O Café ') 
print('::'*20)

