'''
    Faça um programa que tenha uma Função
chamada área(), que receba as dimensões de um
terreno retangular (largura e conprimenta) e
mostra a área do terreno.

'''
while True:
    def área(largura, comprimento):
        a = largura * comprimento
        print(f' A área de um terreno {largura} * {comprimento} é de {a}')
    # Programa principal    
    print(' Controle De Terrenos ')
    print('-'* 20)
    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO '))
    área(l,c)
    resposta = str(input('Quer Avaliar Outro Aluno? [S/N]'))
    if resposta in 'Nn':
        break
print('-='*20)
print('       Pausa Para O Café ')
print('-='*20)


