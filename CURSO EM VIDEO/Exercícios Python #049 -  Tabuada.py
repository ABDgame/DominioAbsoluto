# Desafio 049 - Refaça o Desifio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para ver sua tabuada: ')) 
for c in range(1, 11):
    print('{} × {:2} = {}'.format(num, c, num*c))
# Ok. Deu certo, mas eu que um menu para escolher outra tabuada 
# após aparecer o resultado da primeira tabuada escolhida.


