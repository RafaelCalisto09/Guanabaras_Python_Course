'''
Desafio 14
Faca um programa que converte uma temperatura digitada em C para F
'''

c = float(input('Digite uma temperatura em C: '))
f = c*1.8+32
print('A temperatura de {:.1f}C corresponde em {:.1f}F!'.format(c, f))