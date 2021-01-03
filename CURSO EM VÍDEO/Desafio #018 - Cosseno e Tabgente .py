'''
    Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
while True:
    from math import radians, sin, cos, tan
    angulo = float(input('Digite o ângulo que você deseja: ')) 
    seno = sin(radians(angulo))
    print ('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
    cosseno = cos(radians(angulo))
    print ('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
    tangente = tan(radians(angulo))
    print ('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Ler Outro Ângulo ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café!!!')
