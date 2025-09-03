from datetime import datetime

def tabuada_8():
    # tabuada do 8
    for tabuada in range(0, 101):
        print(f'{tabuada} X 8 = {tabuada * 8}')

ano = datetime.now().year
mes = datetime.now().month
dia = datetime.now().day
hora = datetime.now().hour
minuto = datetime.now().minute
segundo = datetime.now().second

def data_atual():
    print(f'São {hora}:{minuto}:{segundo} do dia {dia} de {mes} de {ano}')
    
while True:
    escolha = int(input('Escolha uma das opções abaixo:\n1. tabuada\n2. data\n'))
    if escolha == 1:
        tabuada_8()
    elif escolha == 2:
        data_atual()
    else:
        print('Opção inválida')
