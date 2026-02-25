#EXERCICIO 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
vlrM = float(input('Escreva aqui um valor em metros -> '))
vlrCm = (vlrM*100)
vlrMm = (vlrM*1000)
print('O valor {} em metros é o mesmo que {} centimetros e {} milimetros'.format(vlrM, vlrCm, vlrMm))
