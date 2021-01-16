'''
     Crie um programa que crie uma matriz de dimensão 
3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a 
formatação correta.
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for lista in range(0,3):
    for coluna in range(0,3):
        matriz[lista][coluna] = int(input(f' Digite um valor para [{lista}, {coluna}]: '))
print('-='*20)
for lista in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[lista][coluna]:^5}]', end='')
    print()
