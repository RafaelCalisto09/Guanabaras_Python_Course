'''
Desafio 12
Faca um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto
'''

p = float(input('Qual o preco do produto? R$'))
print('O produto custava R${}, na promocao com desconto de 5% vai custar R${:.2f}'.format(p, p*.95))