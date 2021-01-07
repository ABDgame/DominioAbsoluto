''' 
 Desafio 053 - Crie um programa que leia
uma frase qualquer e diga se ela é um palindroma,
desconsiderando os espaços.
'''
while True:
    frase = str(input('Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = junto[::-1]
    print('O inverso de {} é {}'.format(junto, inverso))
    if inverso == junto:
        print('Temos um palindromo!')
    else:
        print('A frase digitada não é um palindromo!')
        sair = ' '
    while sair not in 'SN':
        sair = str(input('Digitar Outra Frase ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('        Pausa Para O Café ')
print('::'*20)