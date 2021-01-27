'''
    Faça um programa que tenha uma função chamada ficha(), que
receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
'''
def ficha(jogador='<desconhecido> ', gols=0):
    print(f'O jogador {jogador} fez {gols} no campeonato.')
#Programa Principal
nome = str(input("Nome do Jogador: "))
gol = str(input(" Número de Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
    
