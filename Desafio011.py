'''
Desafio 11
Faca um programa que leia a altura e a largura de uma parede em metros e calcule a sua area
e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta 2 metros quadrados
'''
L = float(input('Largura da parede em metros: '))
A = float(input('Altura da parede em metros: '))
area = L*A
tinta = area/2

print('Sua parede tem a dimensao de {}x{} e sua area é de {}m² \nPara pintar essa parede, voce precisara de {:.2f}l de tinta'.format(L, A, area, tinta))