'''
Desafio 18
Faca um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse angulo
'''

import math
a = float(input('Digite um angulo: '))
arad = math.radians(a)
print('\nO angulo de {} tem o SENO de {:.2f}\nO angulo de {} tem o COSSENO de {:.2f}\nO angulo de {} tem a TANGENTE de {:.2f}!'.format(a, math.sin(arad), a, math.cos(arad), a, math.tan(arad)))
