'''
    Crie uma tupla preenchida com os 20
primeiros colocados da Tabela do Campeonato  
Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
    A - Os 5 primeiros.
    B - Os últimos 4 colocados.
    C - Times em ordem alfabética.
    D - Em que posição está o time
    da Chapacoense.
'''
times = ('Corinthias' , 'Palmeiras','Santos','Grêmio',
	         'Cruzeiro' , 'Flamengo' , 'Vasco', 'Chapecoense',
	         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
	         'São Paulo', 'Fluminense', 'Sport Recife',
	         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
	         'Atlético-GO')
print('::' * 20)
print(f'Lista de Times do Brasileirão: {times}')
print('::' * 20)
print(f'Os 5 Primeiros São {times[0:5]}')
print('::' *20)
print(f'Os 4 Últimos São {times[-4:]} ')
print('::' *20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('::' *20)
print(f'O Chapecoense está na {times.index("Chapecoense")} posição')
