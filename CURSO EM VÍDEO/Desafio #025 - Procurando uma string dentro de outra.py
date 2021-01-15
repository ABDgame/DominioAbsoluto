'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem 
"MARIA" no nome.
'''
while True:
    nome = str(input('Qual é o nome completo? ')).strip()
    print('Seu nome tem Maria? {}'.format('Rosa' in nome))
    resposta = str(input('Quer Continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-='*20)
print('        Pausa Para O Café ')
print('-='*20)
    	
     