'''
     Faça um mini-sistema que utilize o interactive Help do Python,
O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
'''
from time import sleep
c = ('\033[n' ,        # 0 = sem cores
	    '\033[0;30;41m',  # 1 = vermelho 
	    '\033[0;30;42m',  # 2 = verde
	    '\033[0;30;43m',  # 3 = amarelo
	    '\033[0;30;44m',  # 4 = azul
	    '\033[0;30;45m',  # 5 = roxo
	    '\033[7;30m'      # 6 = branco
	    );
def ajuda(com):
    título(f'Acessando O Manual Do Comando \'{com}\'', 4)
    print(c[6], end='')
    help[com]
    print(c[0], end='')
    sleep(2)
    
    
def título(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(c[cor], end='')
    print('=-' * tamanho)
    print(f '{mensagem}')
    print('-=' * tamanho)
    print(c[0], end='')
    sleep(1)
    

# Programa Principal 
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input(" Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Pausa Merecida Para O Café!',1)
    
