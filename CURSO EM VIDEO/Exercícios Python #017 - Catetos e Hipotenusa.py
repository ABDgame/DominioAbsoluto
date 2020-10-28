#Faça um programa que leia o comprimento do 
#cateto oposto e do cateto adjacente de um
#triangulo retangulo, calcule e mostre o
#comprimento da hipotenusa.
from math import hypot
oposto = float(input('Comprimento do cateto oposto: ')) 
adjacente  = float(input('Comprimento do cateto adjacente: ')) 
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
