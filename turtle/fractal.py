## desde https://www.youtube.com/watch?v=9PW_m_ffOWY
import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

random_colors = ["#FFA07A", "#A9F5F2", "#F5A9F2", "#F5F6CE", "#D0A9F5", "#4DD1B2"]

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.left(90)

def dibujarArbol(tamanoDeRama, tortuga):
    tortuga.pensize(tamanoDeRama/10)
    if (tamanoDeRama < 40):
        tortuga.dot(random.randint(7, 10), random.choice(random_colors))
        return
    tortuga.forward(tamanoDeRama)
    tortuga.left(30)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga)
    tortuga.right(60)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga)
    tortuga.left(30)
    tortuga.backward(tamanoDeRama)

tortuga.penup()
tortuga.setpos(0, -350)
tortuga.pendown()
tortuga.hideturtle()
tortuga.color("#ACEE3F")
dibujarArbol(200, tortuga)

# LUCES
maxY = 250
maxX = 350
luces = []

for j in range(0, 100):
    y = random.randint(-1*maxY, maxY)
    x = random.randint(-1*maxX, maxX)
    luz = turtle.Turtle()
    luz.speed(0)
    luz.hideturtle()
    luz.penup()
    luz.setpos(x, y)
    luz.pendown()
    luz.dot(random.randint(1, 5), random.choice(random_colors))
    luces.append(luz)
    if len(luces) > 150:
        luzAApagar = random.choice(luces)
        luzAApagar.clear()

window.exitonclick()