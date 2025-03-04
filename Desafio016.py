'''
Desafio 16
Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira
ex: digite um numer: 6.127
O numero 6.127 tem a parte inteira 6.
'''

import math

n = float(input('Digite um valor: '))
nint = int(n // 1)
print('Usando divisao inteira!')
print('O numero {} tem a sua parte inteira de {}'.format(n, nint))

print('\nOutra forma de fazer, usando trunc!')
print('O numero {} tem a sua parte inteira de {}'.format(n, math.trunc(n)))

print('\nOutra forma de fazer usando int')
print('O numero {} tem a sua parte inteira de {}'.format(n, int(n)))