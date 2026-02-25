#EXERCICIO 11
# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
#LARGURA = L, ALTURA = at, AREA = ar, QUANTIDADE DE TINTA = T
print('Ola! para saber a quantidade de tinta necessaria pra pintar sua parede, preciso que digite alguns dados a seguir.')
L = float(input('Digite aqui a largura da parede em M (só numeros) -> '))
at = float(input('Digite aqui a altura da parede em M (só numeros) -> '))

ar = float(L*at)
t = float(ar/2)
print('A área total da sua parede é de {} M², e para pinta-la toda serão necessários {} litros de tinta'.format(ar,t))