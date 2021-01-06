''' 
    Desafio #043 - Índice de Massa Corporal 
 Desenvolva uma lógica que leia o peso e altura de uma pessoa,
 calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
 - Abaixo de 18.5: Abaixo do Peso
 - Entre 18.5 e 25: Peso ideal
 - 25 até 30: Sobrepeso
 - 30 até 40: Obesidade 
 - Acima de 40: Obesidade mórbida
'''
while True:
    peso = float(input('Digite seu peso atual: '))
    altura = float(input('Digite sua altura: '))
    imc = peso / (altura ** 2)
    print('O IMC desta pessoa é de {: 1f}'.format(imc))
    if imc < 18.5:
        print ('Você está ABAIXO DO PESO ideal')
    elif 18.5 <= imc < 25:
        print ('Você está PESO ideal')
    elif 25 <= imc < 30:
        print ('Você está com sobrepeso  ')
    elif 30 <= imc < 40:
        print ('Você está com obesidade  ')
    elif imc > 40:
        print ('Você está com obesidade mórbida ')
