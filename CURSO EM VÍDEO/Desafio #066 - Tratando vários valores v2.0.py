'''
     Atualização do Exercício Python #064
'''
soma = 0
contador = 0
while True:
    número = int(input('Digite um número inteiro (999 se quiser parar): '))
    if número == 999:
        break
    contador += 1
    soma += número
print(f'Você digitou {contador} números e a soma entre eles foi {soma}! ')
