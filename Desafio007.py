'''
Desafio 7
Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua media
'''

n1 = float(input('Primeira nota do Aluno: '))
n2 = float(input('Segunda nota do Aluno: '))
m = (n1+n2)/2
print('A media entre a primeira nota {:.1f}, e a segunda nota {:.1f}, é: {:.1f}'.format(n1, n2, m))