'''
Desafio006 - Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada.
'''

n = int( input('Digite um numero: '))
print('Anaisando o numero {}, seu Dobro é {}, seu triplo é {}, e sua raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))