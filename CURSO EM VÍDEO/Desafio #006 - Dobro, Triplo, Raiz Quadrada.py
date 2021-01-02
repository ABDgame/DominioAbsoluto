'''  
    Crie um algoritmo que leia um número e mostre o seu dobro
triplo e raiz quadrada.
'''
while True:
    valor = int(input('Digite um número: '))
    dobro = valor * 2 
    triplo = valor * 3
    raizquadrada = valor ** (1/2)
    print('O dobro de {} vale {}. '.format(valor, dobro ))
    print('O triplo de {} vale {}.'.format(valor, triplo))
    print('A raiz quadrada de {} vale {}.'.format(valor, raizquadrada))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Valor? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    

