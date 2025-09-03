import turtle, time


tela = turtle.Screen()
tartaruga = turtle.Turtle()
texto_tartaruga = turtle.Turtle()
texto_tartaruga.hideturtle()
texto_tartaruga.penup()


def desenhar_linhas_e_texto():
   tartaruga.clear()
   tartaruga.penup()
   tartaruga.goto(0, 0)
   tartaruga.pendown()


   comprimento_total = 0  # Comprimento total da linha
   for i in range(0, 301, 10):
       print(i)
       tartaruga.forward(10)  # Move 10 pixels por vez


       texto_tartaruga.clear()
       texto_tartaruga.goto(0, -tela.window_height() / 2 + 20)  # Posição fixa no rodapé
       texto_tartaruga.write(str(i), align="center", font=("Arial", 12, "normal"))




def main():
   tela.setup(800, 600)
   tela.bgcolor("lightgray")
   tela.title("Desenho com Loop e Texto Interativo")


   tartaruga.shape("turtle")
   tartaruga.color("blue")
   tartaruga.speed()
   tartaruga.pensize(30)


   tela.onkeypress(desenhar_linhas_e_texto, "space")
   tela.listen()
   tela.mainloop()


if __name__ == '__main__':
   main()
