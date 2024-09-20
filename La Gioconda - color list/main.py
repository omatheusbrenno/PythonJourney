import turtle as turtle_module
import random

# Configurações iniciais do turtle
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Lista de cores
color_list = [(18, 19, 26), (30, 21, 26), (45, 30, 24), (86, 101, 92), (33, 41, 38),
              (124, 87, 63), (207, 150, 102), (72, 86, 90), (129, 145, 125), (90, 53, 44),
              (137, 135, 100), (55, 69, 64), (119, 135, 115), (251, 202, 148), (244, 187, 131),
              (187, 110, 74), (78, 66, 43), (54, 68, 70), (86, 50, 54), (96, 60, 63),
              (57, 63, 72), (134, 145, 147)]

# Posição inicial do turtle
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

# Número de pontos
number_of_dots = 66
color_index = 0  # Índice inicial da lista de cores

# Desenho dos pontos
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, color_list[color_index])
    tim.forward(50)

    # Muda para a próxima cor na lista
    color_index += 1
    if color_index == len(color_list):  # Se atingir o fim da lista, recomeça
        color_index = 0  # Reinicia o índice

    # Mudança de linha a cada 10 pontos
    if dot_count % 10 == 0:
        tim.setheading(90)  # Vira para cima
        tim.forward(50)     # Move para a linha de cima
        tim.setheading(180) # Vira para a esquerda
        tim.forward(500)    # Retorna à posição inicial da nova linha
        tim.setheading(0)   # Vira para a direita para continuar os pontos

# Mantém a tela aberta
screen = turtle_module.Screen()
screen.exitonclick()
