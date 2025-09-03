import turtle

# Losangolo
def desenhar():
   tartaruga = turtle.Turtle()
   tartaruga.goto(0, 0)
   tartaruga.color('green')
   tartaruga.speed('slow')
   tartaruga.right(45)
   tartaruga.left(90)
   tartaruga.forward(300)
   tartaruga.left(90)
   tartaruga.forward(300)
   tartaruga.left(90)
   tartaruga.forward(300)
   tartaruga.left(90)
   tartaruga.forward(300)

# if __name__ == '__main__':
#    tela = turtle.Screen()
#    desenhar()
#    tela.mainloop()


def linha_pontilhada():
   tar = turtle.Turtle()
   tar.penup()
   tar.goto(-500, 0)
   tar.color('green')
   tar.speed('fast')
   for x in range(-500, 500):
        if x % 5 == 0:
            tar.pendown()
        else:
            tar.penup()
        tar.goto(x, 0)

linha_pontilhada()