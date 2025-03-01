'''
Desafio 13
Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
'''

s = float(input('Qual é o salario do funcionario? R$'))
print('Um funcionario ganhava R${:.2f}, com 15% de aumento passou a receber R${:.2f}.'.format(s, s*1.15))