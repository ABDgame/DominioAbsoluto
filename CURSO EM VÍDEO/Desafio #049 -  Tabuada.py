'''
   Desafio 049 - Refaça o Desifio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''
while True:
    num = int(input('Digite um número para ver sua tabuada: ')) 
    for c in range(1, 11):
        print('{} × {:2} = {}'.format(num, c, num*c))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Analisar outro nome ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')    



