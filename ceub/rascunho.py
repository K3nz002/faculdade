# # x = 7
# # y = 13
# # if x < y:
# #     x *= 3
# # if x > 7 and y == 13:
# #     y = x + y
# # if y < x:
# #     x = 10
# # print (x + y)

# # nomes = ["Ana", "Pedro", "Maria", "Lucas", "Sofia", "Gabriel", "Laura", "Mateus", "Isabela", "Enzo"]

# # tamanho_total = 0
# # for nome in nomes:
# #     tamanho_total += len(nome)

# # print(tamanho_total)

# # lista = ['Arroz', 'Feijão', 'Macarrão', 'Sal']
# # indice = 0
# # soma = 0
# # while indice < len(lista):
# #     soma +=len(lista[indice])
# #     indice += 1
# # print(soma)

# import turtle

# tela = turtle.Screen()
# tartaruga = turtle.Turtle()
# tartaruga.penup()

# def quadrado():
#     pixel = 5
#     tartaruga.reset()
#     tartaruga.penup()
#     tartaruga.goto(800, 100)
#     tartaruga.pendown()
#     tartaruga.speed()
#     for i in range(0, 1000, 5):
#         tartaruga.forward(pixel)
#         pixel += 5
#         tartaruga.right(90)

# def circulo():
#     pixel = 5
#     tartaruga.reset()
#     tartaruga.penup()
#     tartaruga.goto(-800, 0)
#     tartaruga.pendown()
#     tartaruga.speed()
#     for i in range(0, 1000, 5):
#         tartaruga.circle(pixel)
#         pixel += 5
    


# def main():
#    tela.setup(800, 600)
#    tela.bgcolor("lightgray")
#    tela.title("Desenho com Loop e Texto Interativo")

#    tartaruga.shape("turtle")
#    tartaruga.color("blue")
#    tartaruga.speed()
#    tela.onkeypress(quadrado, "space")
#    tela.onkeypress(circulo, "=")
#    tela.listen()
#    tela.mainloop()


# if __name__ == '__main__':
#    main()

# def calcular_saldo(transacoes):
#     saldo = 0
#     for valor in transacoes:
#       saldo_final = sum(valor)
#     print(f'R$ {saldo_final: .2f}')

# entrada_usuario = input()

# entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

# transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# # TODO: Calcule o saldo com base nas transações informadas:
# resultado = calcular_saldo(transacoes)

# print(resultado)

entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]
print(transacoes)