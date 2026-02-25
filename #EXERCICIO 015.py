#EXERCICIO 15
# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

print('Bem vindo ao Sistema da Concessionaria de Carros X')
print('Por favor, para devolver o carro preencha as seguintes informações...')
K=float(input('Qual foi a quilometragem percorrida? ->'))
D=float(input('Quantos dias você passou com o carro? ->'))
PD=60*D #Preço do Dia
PK=0.15*K #Preço da Quilometragem
PF= PD+PK #Preço Final
print('O Valor do seu aluguel é de: R$',(PF))