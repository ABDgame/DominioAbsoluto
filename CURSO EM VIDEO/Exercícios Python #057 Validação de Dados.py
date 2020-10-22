# Desafio 057 - Faça um programa que leia o genero de uma
# pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peça digitação novamente até 
# ter um valor correto.
genero = str(input('Informe seu gênero:[M/F]')).strip().upper()[0]
while genero not  in 'MmFf' :
    genero = str(input(' Dados inválidos. Por favor, informe seu gênero: ')). strip().upper()[0]
print('Gênero {} registrado com sucesso'.format(genero))


