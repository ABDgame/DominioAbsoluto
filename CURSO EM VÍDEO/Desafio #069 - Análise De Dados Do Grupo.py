'''
    Desafio 069
    Crie um programa que leia a idade e o
gênero de vários pessoas. A cada
pessoa cadastrada, o programa 
deverá perguntar se o usuário quer
ou não continuar. No final, mostre:
    - Quantas pessoas tem mais de 18 anos.
    - Quantos homens foram cadastrados.
    - Quantas mulheres tem menos de 20 anos.
'''
print('-='*20)
print('          Análise De Dados Do Grupo')
print('-='*20)

total18 = totalHomem = totalMulher20 = 0
while True:
    idade = int(input('Idade: '))
    gênero = ' '
    while gênero not in 'MF':
        gênero = str(input('Gênero: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if gênero == 'M':
        totalHomem += 1
    if gênero == 'F' and idade < 20:
        totalMulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer Continuar ?')).strip().upper()[0]
    if resposta == 'N':
        break
print ('::'*20)
print (f' Total de pessoas com mais de 18 anos: {total18}')
print (f' Ao todo temos {totalHomem} homens cadastrados')
print (f' E temos {totalMulher20} mulheres com menos de 20 anos')
print ('::'*20)
print ('           Pausa Para O Café  ')
    
