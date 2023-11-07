import turtle 


def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color="grey",
        walls_w=100,
        walls_h=150,
        walls_color="red",
        roof_w=100, 
        roof_h=70, 
        roof_color="black"
    ):
    draw_base(x, y, base_w, base_h, base_color)
    draw_walls()
    draw_roof


def draw_base(x, y, base_w, base_h, base_color):
    print("Рисует фундамент")
    print(base_color)
    draw_rectangle(y, x, base_w, base_h, base_color)

def draw_walls():
    print("Рисует стены")


def draw_roof():
    print("Рисует крышу")


def draw_rectangle(y, x, width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()



draw_house(base_color="red")


turtle.done()