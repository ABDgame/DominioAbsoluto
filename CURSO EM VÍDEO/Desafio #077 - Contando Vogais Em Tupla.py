'''
    Crie um programa que tenha uma tupla com vários palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
'''
palavras = ('Abacaxi','Goiaba','Banana', 'Cereja',
	           'Manga', 'Maracujá','Caju','Morango',
	            'Mexerica', 'Melancia', 'Jabuticaba')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos  ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aáâãàeéêiou':
            print(letra.upper(), end=' ')
        
