'''
Desafio 19
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''
import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))

'''
from random import choice

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))
'''