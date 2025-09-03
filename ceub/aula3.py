import math

x = 7
y = 9

print('x + y = ',end = '')
print(x + y)

raio = float(input('Digite o valor do raio em centímetros: '))
area_circunferencia = math.pi * raio ** 2

print(f'A área da circunferencia é{area_circunferencia: .2f} cm')

nome_problema = input('Escreva um nome: ')
qtd_impressoes = int(input('Escreva a quantidade de vezes que você quer que apareça o nome: '))
nome_arq = input('Escreva o nome do arquivo que ficará armazenado os nomes repetidos: ')

nome_problema += '\n'
lista_nome = nome_problema * qtd_impressoes
print(lista_nome)

with open(nome_arq, 'w') as arquivo:
    arquivo.write(lista_nome)
'''
'''

nome = input('Escreva o nome: ')
qtd_nome = int(input('Escreva a quantidade de vezes que irá aparecer: '))
cmd = f'print("{nome}")\n' * qtd_nome

with open('imp.py', 'w') as arquivo:
    arquivo.write(cmd)