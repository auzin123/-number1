name = "Илья Муромец"

way_left = False
way_center = False
way_right = False

while way_left == False or way_center == false or way_right == False:
    
    print(name, "встретил на распутье трех дорог горючий камень с надписью")
    print("Налево поехать - уьитым быть")
    print("Прямо поехать - женатым быть")
    print("Направо поехать =-  богатым быть")

    way = input("Куда поехать?")
    if way == "налево":
        if way_left == False:
            print(name, "убит!")
            way_left = True
        else:
            print(name, "уже был на левой дороге")
    elif way == "прямо":
        print(name, "женат")
        way_center = True
    elif way == "направо":
        print(name, "богат!")
        way_right = True
    else:
        print("Нет такой дороги")
