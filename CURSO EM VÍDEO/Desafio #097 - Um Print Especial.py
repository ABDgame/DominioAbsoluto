'''
    Faça um programa que tenha uma função
chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex
escreva(Olá Mundo!)
Saída
Olá Mundo!

'''
def escreva(msg):
    tamanho = len(msg) + 4
    print('~'* 20)
    print(f' {msg}')
    print('~'* 20)
#while True:
#Programa Principal    
escreva('Débora Inocêncio')
escreva('Python')
escreva('CSS')
escreva('Javascript')
escreva('HTML')