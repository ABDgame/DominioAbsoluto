'''
Desafio 016
'''
while True:
    import math
    número = int(input('Digite um número: '))
    raiz = math.sqrt(número)
    print('A raiz de {} é igual a {:.2f}'.format(número,raiz))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Digitar Outro Número ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')