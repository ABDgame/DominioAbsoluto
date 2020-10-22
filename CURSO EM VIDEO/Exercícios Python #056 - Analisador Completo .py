# Desafio 056 - Desenvolva um programa que leia o nome,
# idade e gênero das 4 pessoas.No final do programa, mostre:
# - A média de idade do grupo.      - Quantas mulheres têm menos de 20 anos.
# - Qual é o nome do homem mais velho. 
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('-------- {}° JOGADOR -------- '.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero: ')).strip()
    somaidade += idade
    if pessoa == 1 and genero in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Ff' and idade < 20:
       totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade dos jogadores é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))  
