'''
Desafio 17
Faca um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo.
calcule e mostre o comprimento da hipotenusa.
'''

import math

print('Calcuando na raca')
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto adjascente: '))
h = ((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))
print('A hipotenusa vai ser pelo python {:.2f}'.format(math.hypot(co, ca)))