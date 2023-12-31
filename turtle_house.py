import turtle 


def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color="grey",
        walls_w=100,
        walls_h=110,
        walls_color="red",
        roof_w=100, 
        roof_h=80, 
        roof_color="black"
    ):
    draw_base(x, y, base_w, base_h, base_color)
    walls_y = y + base_h 
    draw_walls(x, walls_y, walls_w, walls_h, walls_color)
    roof_y = walls_y + walls_h
    draw_roof(x, roof_y, roof_w, roof_h, roof_color, walls_w)


def draw_base(x, y, base_w, base_h, base_color):
    print("Рисует фундамент")

    draw_rectangle(y, x, base_w, base_h, base_color)

def draw_walls(x, y, walls_w, walls_h, walls_color):
    draw_rectangle(x, y, walls_w, walls_h, walls_color)


def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w,):
    turtle.goto(x, y)
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    top_x = walls_w // 2
    top_y = y + roof_h
    turtle.goto(top_x, top_y)
    right_x = x + walls_w
    turtle.goto(right_x, y)
    turtle.goto(x, y)
    turtle.end_fill()


def draw_rectangle(x, y, width, height, color):
    turtle.goto(x, y)
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



draw_house(base_color="purple")


turtle.done()

