'''
Desafio 10
Crie um programa que leia quanto dinheiro a pessoa tem na carteira e quantos dolares ela pode comprar
Dolar=3.27
'''

m = float(input('Quanto dinheiro voce tem na carteira? R$'))
d = float(input('Quanto esta a cotacao do dolar hoje?'))
print('Com o dinheiro que voce tem na carteira, voce pode comprar ${:.2f} dolares'.format(m/d))