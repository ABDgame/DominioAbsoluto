'''
     Aprimore corretamente (o meu anterior, contou errado os gols) 
o Desafio #093. Este realmente funciona com vários jogadores,
inclui um sistema de visualização de detalhes do aproveitamento
de cada jogador.

'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome Do Jogador: '))
    total = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for chave in range(0, total):
        partidas.append(int(input(f'  Quantos Gols Na Partida {chave+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas com as letras S ou N.')
    if resposta == 'N':
        break
print('::' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()            
print('-=' * 20)
for chave, valor in enumerate(time):
    print(f'{chave:>3}',end='')
    for dado in valor.values():
        print(f' {str(dado):<15}', end='')
    print()
print('-=' * 20)
while True:
    busca = int(input('Mostrar Dados De Qual Jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, gol in enumerate(time[busca]['gols']):
            print (f'   No Jogo {i+1} fez {gol} gols.')
    print('-='*20)
print('::::::::      Pausa Para O Café     :::::::: ' )

     
    

    


         

