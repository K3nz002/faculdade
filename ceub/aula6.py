# print(list(range(10, 0, -1)))

# def add_lista():
#     lista = ['sla']
#     while True:
#         indice = input('Escreva o que você quer add na lista: ')
#         if indice == 'sair':
#             break
#         if indice == lista:
#             lista.reverse()
#             lista.pop()
#             print('Você já add esse elemento na lista')
#         lista.append(indice)
#         print(lista)

# add_lista()

# Lista de Compras

lista = []

def add_item():
    produto = input('Nome do produto: ').lower()
    quantidade = int(input('Quantia do produto: '))
    preco = float(input('Preço do produto: '))
    total = quantidade*preco
    item = (produto, quantidade, preco, total)
    lista.append(item)

def imprimir_item():
    num_item = 0
    for item in lista:
        num_item += 1
        print(f'Número do produto: {num_item}, Produto: {item[0]}, Quantidade: {item[1]}, Preço: R$ {item[2]}, Total: R$ {item[3]: .2f}')

def remover_item():
    imprimir_item()
    item = int(input('Qual produto você quer remover: '))
    lista.pop(item)

def main():
    while True:
        escolha = int(input('Escolha o que você quer fazer:\n1. Adicionar produto\n2. Remover produto\n3. Imprimir produto\n4. Sair\n'))
        
        match escolha:
            case 1:
                add_item()
            case 2:
                remover_item()
            case 3:
                imprimir_item()
            case 4:
                print('O programa terminou')
                break

# Execução do programa
main()