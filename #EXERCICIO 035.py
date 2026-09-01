#EXERCICIO 035

# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.
print('---=---' *12)
print ('Olá! Digite aqui três medidas para saber se o triãngulo pode ser formado!')
print('---=---' *12)
l1 = int(input('Primeira medida -> '))
print('---=---' *12)
l2 = int(input('Segunda medida -> '))
print('---=---' *12)
l3 = int(input('Terceira medida -> '))
print('---=---' *12)
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print ('OPA! Isso é um triângulo!')
    print('---=---' *12)
    if l1 == l2 == l3:
        print ('E esse triângulo é equilátero!')
    if l1 == l2!= l3 or l1 == l3!= l2 or l2 == l3!= l1:
        print ('E esse triângulo é isóceles!')
    elif l1!= l2!= l3:
        print ('E esse triângulo é escaleno!')
else:
    print ('EITA! Isso não pode ser um triângulo!')

print('---=---' *12)