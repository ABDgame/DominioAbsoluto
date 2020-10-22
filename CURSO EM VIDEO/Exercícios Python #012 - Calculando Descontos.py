# Desafio 012
preço = float(input('Quanto é o preço do seu produto? R$'))
novo = preço - (preço * 5/ 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))