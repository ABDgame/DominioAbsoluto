'''
    Desenvolva um programa que
leiw quatro valores pelo teclado e
guarde-os em uma tupla. No final,
mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
'''
números = (int(input('Digite um número: ')),
	         int(input('Digite outro número: ')),
	         int(input('Digite mais um número: ')),
	         int(input('Digite o último número: ')))
print(f'Você digitou os valores {números}')
print(f'O valor 9 apareceu {números.count(9)} vezes')
if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3)}° lugar')
else:
    print('O valor 3 não foi digitado em nenhum lugar')
print('Os valores pares digitados foram ', end=' ')
for número in números:
    if número % 2 == 0:
        print(número, end=' ')



