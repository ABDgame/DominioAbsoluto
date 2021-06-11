print('-='*20)
print('        Abastecimento Fórmula 1  ')
print('-='*20)
while True:
    Pista = float (input ('Qual  o  comprimento da pista em metros? '))
    Voltas = float (input('Quantas voltas serão percorridas? '))
    QuantidadeAbastecimentos  = float (input('Quantas vezes será reabastecido? '))
    Consumo  = float (input('	Qual o consumo de combustivel (km/L)?'))
    VoltasPrimeiraParada = Voltas / QuantidadeAbastecimentos
    PrimeiroReabastecimento = VoltasPrimeiraParada * (pista/1000) * Consumo
    print('Total de combustivel ate o 1º reabastecimento', PrimeiroReabastecimento ,'Litros')
    
    
