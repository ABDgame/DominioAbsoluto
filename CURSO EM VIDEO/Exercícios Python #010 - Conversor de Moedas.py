# Desafio 010 - Conversor de moedas
real = float(input('Quanto de dinheiro, você tem na carteira? R$'))
dolar = real / 4.31
euro = real / 4.81
print ('Com R${:.2f} você pode comprar U$${:.2f} e €{:.2f}'.format(real, dolar, euro ))
