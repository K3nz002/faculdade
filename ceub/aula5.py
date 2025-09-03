


def verificador():
    valor = int(input('Digite o valor para verificar se ele é par e positivo: '))
    if valor == 0:
        print(f'{valor} é nulo')
    elif valor % 2 == 0 and valor > 0:
        print(f'O {valor} é par e positivo')
    elif valor % 2 != 0 and valor < 0:
        print(f'O {valor} é ímpar e negativo')
    elif valor % 2 != 0 and valor > 0:
        print(f'O {valor} é ímpar e positivo')
    else:
        print(f'O {valor} é par e negativo')

def faixa_etaria():
    idade = int(input('Digite a idade que você quer verificar: '))
    if 18 <= idade <= 65:
        print(f'Está dentro da faixa etária econômicamente ativa')
    else:
        print(f'Está fora da faixa etária econômicamente ativa')

def ano_bissexto():
    ano = int(input('Digite o ano que você quer verificar se é bissexto: '))
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        print(f'O {ano} é bissexto')
    else:
        print(f'O {ano} não é bissexto')
    


escolha = int(input('Escolha o que você quer verificar:\n1. verificador de valor\n2. verificador de faixa etária\n3. verificador de ano bissexto\n'))

match escolha:
    case 1:
        verificador()
    case 2:
        faixa_etaria()
    case 3:
        ano_bissexto()