import turtle 
from random import randint
turtle.speed(0)

turtle.colormode(255)

def draw_house(
        x=-400,
        y=0,
        base_w=40,
        base_h=10,
        base_color="grey",
        walls_w=40,
        walls_h=50,
        walls_color="red",
        roof_w=50, 
        roof_h=30, 
        roof_color="green"
    ):
    draw_base(x, y, base_w, base_h, base_color)
    walls_y = y + base_h 
    draw_walls(x, walls_y, walls_w, walls_h, walls_color)
    roof_y = walls_y + walls_h
    draw_roof(x, roof_y, roof_w, roof_h, roof_color, walls_w)

def draw_base(x, y, base_w, base_h, base_color):

    draw_rectangle(x, y, base_w, base_h, base_color)

def draw_walls(x, y, walls_w, walls_h, walls_color):
    draw_rectangle(x, y, walls_w, walls_h, walls_color)


def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w,):
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    turtle.goto(x,  y)
    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)
    top_x = x + walls_w // 2
    top_y = y + roof_h
    turtle.goto(top_x, top_y)
    left_x = top_x - roof_w // 2
    turtle.goto(left_x, y)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
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


def draw_street(house_x=-400, house_y=0, houses=10):
    counter = 0
    while counter < houses:
        base_w = randint(50, 50)
        walls_w = randint(base_w - 3, base_w)
        roof_w = randint(walls_w, walls_w + 3)
        draw_house(
            x=house_x,
            y=house_y,
            base_w=randint(30, 50),
            base_h=randint(10, 20),
            base_color=(randint(0,255), randint(0,255), randint(0,255)),
            walls_w=randint(30, 50),
            walls_h=randint(30, 50),
            walls_color=(randint(0,255), randint(0,255), randint(0,255)),
            roof_w=roof_w,
            roof_h=randint(30, 50),
            roof_color=(randint(0,255), randint(0,255), randint(0,255)),
        )
        counter += 1
        house_x += roof_w // 2 + base_w

draw_street(-700, 0, 20)

turtle.done()
