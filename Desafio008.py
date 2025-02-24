'''
Desafio 8
Escreva um programa que leia o valor em metros e exiba convertido em centimetros e milimetros
'''

medida = float(input('Insira uma medida em metros please! '))
cm = medida*100
mm = medida*1000
print('{} metros equivale em centimetros, a {:.0f} centimetros \n{} metros equivale em milimetros, a {:.0f} milimetros'.format(medida, cm, medida, mm))