'''
    Crie um programa onde o usuário digite uma expressão 
qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e
fechados na ordem correta.
'''
expressão =str(input('Digite uma expressão matemática  : '))
pilha = []
for símbolo in expressão:
    if símbolo == ' ( ':
        	pilha.append(' ( ')
    elif símbolo == ')':
        if len(pilha) > O:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está VÁLIDA!')
else:
    print('Sua expressão está ERRADA')

            


