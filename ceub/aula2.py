import numpy
import requests

# area do triangulo
base = 10
altura = 5
area_triangulo = (base * altura) / 2

print(area_triangulo)


def calculadora():
    primeiro_valor = float(input('Digite o primeiro valor: '))
    segundo_valor = float(input('Digite o segundo valor: '))
                                        
    soma = primeiro_valor + segundo_valor
    subtracao = primeiro_valor - segundo_valor
    multiplicacao = primeiro_valor * segundo_valor
    divisao = primeiro_valor / segundo_valor
    print(f'A soma é:\n{primeiro_valor} + {segundo_valor} = {soma: .2f}')
    print(f'A subtração é:\n{primeiro_valor} - {segundo_valor} = {subtracao: .2f}')
    print(f'A mutiplicação é:\n{primeiro_valor} x {segundo_valor} = {multiplicacao: .2f}')
    print(f'A divisão é:\n{primeiro_valor} : {segundo_valor} = {divisao: .2f}')

def cotacao_moedas():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    url = requests.get(url)
    lista_moedas = url.json()
    cotacao_dolar = float(lista_moedas['USDBRL']['bid'])
    cotacao_euro = float(lista_moedas['EURBRL']['bid'])
    cotacao_btc = float(lista_moedas['BTCBRL']['bid'])

    print('Escolha uma moeda:\n1. Dólar\n2. Euro\n3. Bitcoin')
    moeda = int(input())
    match moeda:

        case 1:
            print('Escolha a operação que gostaria de fazer\n1. USD -> Real\n2. Real -> USD')
            operacao = int(input())
            match operacao:

                case 1:
                    valor_dolar = float(input('Digite o valor em dólar: '))
                    print(f'O valor de dólar para real é R${valor_dolar * cotacao_dolar: .2f}')

                case 2:
                    valor_real = float(input('Digite o valor em real: '))
                    print(f'O valor de real para dólar é ${valor_real / cotacao_dolar: .2f}')

        case 2:
            print('Escolha a operação que gostaria de fazer\n1. EUR -> Real\n2. Real -> EUR')
            operacao = int(input())
            match operacao:

                case 1:
                    valor_euro = float(input('Digite o valor em euro: '))
                    print(f'O valor de euro para real é R${valor_euro * cotacao_euro: .2f}')

                case 2:
                    valor_real = float(input('Digite o valor em real: '))
                    print(f'O valor de real para euro é €{valor_real / cotacao_euro: .2f}')

        case 3:
            print('Escolha a operação que gostaria de fazer\n1. BTC -> Real\n2. Real -> BTC')
            operacao = int(input())
            match operacao:

                case 1:
                    valor_btc = float(input('Digite o valor em bitcoin: '))
                    print(f'O valor de bitcoin para real é R${valor_btc * cotacao_btc: .2f}')

                case 2:
                    valor_real = float(input('Digite o valor em real: '))
                    print(f'O valor de real para bitcoin é ₿{valor_real / cotacao_btc}')


opcao = int(input('Escolha uma opção:\n1. Calculadora simples\n2. Cotação de moedas\n'))

match opcao:
    case 1:
        calculadora()
    case 2:
        cotacao_moedas()

