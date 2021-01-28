'''
    Crie um programa que tenha a função leiaInt(), que vai funcionar 
de forma semelhante à função input() do Python, só que 
fazendo a validação para aceitar apenas um valor numérico.
Ex:
    número=leiaInt('Digite um número')
'''
def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        número = str(input(mensagem))
        if número.isnumeric():
            valor = int(número)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
     
# Programa Principal         
número = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {número}')

