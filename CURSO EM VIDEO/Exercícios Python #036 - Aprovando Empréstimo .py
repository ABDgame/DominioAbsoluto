# Exercício Python 036 - Escreva um programa para aprovar o empréstimo 
# bancário para a compra de uma casa. Pergunte o valor da casa, o salário do 
# comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo
# será negado.
casa = float(input ( ' Valor da casa: R$ ?'))
salário = float (input ( ' Salário do comprador: R$ ?'))
anos = int(input ( ' Quantos anos de financiamento ? '))
prestação = casa / (anos * 12)
mínimo = casa / (anos * 12)
print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print (	'a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser Concedido! ')
else:
    print('Empréstimo Negado!')