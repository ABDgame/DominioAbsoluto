'''
   Desenvolva um programa que leia o comprimento 
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.

'''
print('-='*20)
print('        Analisador de Triângulo')
print('-='*20)
while True:
    r1 = float(input('Primeiro segmento: '))
    r2 = float(input('Segundo segmento: '))
    r3 = float(input('Terceiro segmento: '))
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos acima PODEM FORMAR triângulo!')
    else:
        print('Os segmentos acima NÃO PODEM FORMAR triângulo')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Calcular Outro Triângulo ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('::'*20)
print('          Pausa Para O Café!!!    ')
print('::'*20)
    
