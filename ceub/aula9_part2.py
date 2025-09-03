import turtle


tela = turtle.Screen()
tartaruga = turtle.Turtle()
passo = 5
limite_aumentar_passo = 20
limite_diminuir_passo = 4


# Funções de movimento
def mover_frente():
   tartaruga.forward(passo)




def mover_tras():
   tartaruga.backward(passo)




def mover_esquerda():
   tartaruga.left(passo)




def mover_direita():
   tartaruga.right(passo)




# Funções para mudar a cor
def mudar_vermelho():
   tartaruga.color("red")




def mudar_verde():
   tartaruga.color("green")




def mudar_azul():
   tartaruga.color("blue")

def aumentar_passo():
    global passo, limite_aumentar_passo

    if passo == limite_aumentar_passo:
        passo == 20
    else:
       passo += 1


def diminuir_passo():
    global passo, limite_diminuir_passo
    if passo == limite_diminuir_passo:
        passo == 5
    else:
       passo -= 1


def main():
   # Configurações da tela
   tela.setup(800, 600)
   tela.bgcolor("lightgray")
   tela.title("Controle da Tartaruga")


   # Configurações da tartaruga
   tartaruga.shape("turtle")
   tartaruga.color("blue")
   tartaruga.speed('fast')  # Velocidade de movimento


   # Configurações de eventos de teclado
   tela.onkeypress(mover_frente, "Up")
   tela.onkeypress(mover_tras, "Down")
   tela.onkeypress(mover_esquerda, "Left")
   tela.onkeypress(mover_direita, "Right")


   # Configurações de eventos de teclado para mudar a cor
   tela.onkeypress(mudar_vermelho, "r")
   tela.onkeypress(mudar_verde, "g")
   tela.onkeypress(mudar_azul, "b")

   # Configuração dos passos da tartaruga 
   tela.onkeypress(aumentar_passo, "=")
   tela.onkeypress(diminuir_passo, "-")

   # Permite que a tela escute os eventos de teclado (as setas e as cores)
   tela.listen()


   # Mantém a tela aberta
   tela.mainloop()




if __name__ == '__main__':
   main()
