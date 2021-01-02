'''
   Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.

   Considere USS 1,00 = R$ 5.22
             € = R$ 6.37
             £ = R$ 7.08
   
          
'''   
while True:
    Real = float(input('Quanto de dinheiro, você tem na carteira? R$'))
    Dolar = Real / 5.22
    Euro = Real / 6.37
    LibraEsterlina = Real / 7.08
    print ('Com R${:.2f} você pode comprar U$${:.2f} , €{:.2f} e £{:.2f}'.format(Real, Dolar, Euro, LibraEsterlina ))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Outra Quantidade De Dinheiro ? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Pausa Para O Café !!!')    
