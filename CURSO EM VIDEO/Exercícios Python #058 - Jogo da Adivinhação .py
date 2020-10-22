# Desafio 058 - Melhore o jogo do DESAFIO 028
# onde o computador vai "pensar" em um número 
# entre 0 a 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos 
# palpites foram necessários para vencer.
from random import randint
smartphone = randint(0, 10)
print('Sou seu smartphone... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogadora = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogadora == smartphone:
        acertou = True
    else:
        if jogadora < smartphone:
            print('Chute um número maior...')
        elif jogadora > smartphone:
            print('Chute um número menor...')
            
print ('Acertou com {} tentativas. Parabéns!! '. format(palpites ))
