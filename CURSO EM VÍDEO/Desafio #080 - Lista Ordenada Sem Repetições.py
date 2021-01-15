'''
    Crie um programa onde o usuário possa digitar cinco valores 
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.
'''
lista = []
for contador in range(0, 5):
    número = int(input('Digite um valor: '))
    if contador == 0 or número >lista[-1]:
        lista.append(número)
        print('Adicionado ao final da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if número <= lista[posição]:
                lista.insert(posição, número)
                print(f'Adicionado na posição {posição} da lista...')
                break 
            posição += 1
print('-=' * 20)
print(f'Os valores digitados em ordem foram {lista}')      
            
            
