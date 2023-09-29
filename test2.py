name = "Илья Муромец"

way_left = False
way_center = False
way_right = False

while way_left == False or way_center == false or way_right == False:
    
    print(name, "встретил на распутье трех дорог горючий камень с надписью")
    print("Налево поехать - убитым быть")
    print("Прямо поехать - женатым быть")
    print("Направо поехать =-  богатым быть")

    way = input("Куда поехать? ")
    if way == "налево":
        if way_left == False:
             path = input("Тут вы встретили разбойников, хотите напасть или отступить? ")
             if path == "напасть":
                    print(name, "убит!")
                    break
                    way_left = True
             elif path == "нет":
                   print(name, "отступить!")  
        else:
            print(name, "уже был на левой дороге")
    elif way == "прямо":
        wedding = input("хотите поженится? ")
        if wedding == "да":
            print(name, "женат")
            way_center = True
        elif wedding == "нет":
            print(name, "не женат")
            break
    elif way == "направо":
        trial = input("Чтобы получить богатства нужно пройти испытание, хотите его пройти? ")
        if trial == "да":
            print(name, "богат!")
        elif trial == "нет":
            print(name, "не богат!")
            break
            way_right = True
    else:
        print("Нет такой дороги")
