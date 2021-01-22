'''
     Crie um programa que gerencia o aproveitamento de um jogador 
de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em
cada partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
       
'''
jogador = dict()
partidas = list()
total = 0
valor = 0
gols = 0
i = 0
while True:
    jogador['nome'] = str(input('Nome Do Jogador: '))
    total = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
    for chave in range(0, total):
        partidas.append(int(input(f'  Quantos Gols Na Partida {chave}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)    
    print('-=' * 30)
    print(jogador)
    print('-=' * 30)
    for chave, valor in jogador.items( ):
        print(f' - {chave} é igual a {valor}')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for i, valor in enumerate(jogador['gols']):
        print(f'       => Na Partida {i}, fez {valor} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')
    resposta = str(input('Quer Avaliar Outro Jogador ? [S/N]')).upper()[0]
    if resposta in 'Nn':
        break
print('-='*20)
print('    Pausa Para O Café ')
print('-='*20)

     
    

    


         

