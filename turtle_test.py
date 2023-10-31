import turtle
turtle.speed(1)
turtle.shape("turtle")

def draw_square(side, color):
    counter = 0
    while counter < 4:
        turtle.fd(side)
        turtle.pencolor(color_1)
        turtle.left(90)
        counter += 1


draw_square(100, "red")
draw_square(110, "green")

turtle.done()