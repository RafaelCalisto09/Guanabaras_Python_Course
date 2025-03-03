'''
Desafio 15
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
'''

d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
custo = (d*60)+(km*.15)

print('O carro foi alugado por {} dias, e rodou {:.1f}Km, logo o custo da locacao é de R${:.2f}'.format(d, km, custo))