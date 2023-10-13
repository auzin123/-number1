from random import randint

player_name = input("Как вас зовут?")
player_level = 10
player_hp = 10 *player_level
player_expe = 0

while True:
    print("_________________________")
    print("1 = начать игру")
    print("2 = уйти")
    print("3 = пойти в магазин")
    print("4 = сыграть в казино")
    option = input("Введите номер ответа и нажмите ENTER ")
    if option == "1":
        enemy_name =("GP_228")
        enemy_level = 10
        enemy_hp = 10 * enemy_level
        enemy_expe = 0
        print(player_name, "сразится проитив", enemy_name)

        while True:
            input("Нажмите ENTER чтобы атаковать ")
            player_attack = randint(0, 10) + player_level 
               
            enemy_hp -= player_attack
            print(player_name, "ударил", enemy_name, "на", player_attack, "жизней")
            print("У", enemy_name, "стало", enemy_hp, "жизней")
            if player_hp <= 0:
                print(player_name, "победил!")
                money += 25
                player_expe += enemy_level
                print(player_name, "получил", enemy_level, "опыта")
                if player_expe % 10 == 0:
                    player_level += player_expe // 10
                    player_expe += enemy_level % 10
                    print(player_name,"получил", player_level, "уровень")
                break
            enemy_attack = randint(0, 10) + enemy_level
            player_hp -= enemy_attack
            print(enemy_name, "ударил", player_name, "на", enemy_attack, "жизней")
            print("У", player_name, "стало", player_hp, "жизней")
            if enemy_hp <= 0:
                print(enemy_name, "погиб")
                
            break
                
        print("бой окончен")
    elif option == "2":
        print("игра окончена")
        break
    elif option == "3":
        print("Вот список всех товаров")
        print("Восстановить все хп = 25 гноп")
        print("Купить бафф к колличеству хп = 100 = гноп")
    elif option == "4":
        from random import randint
        
print("Ваш баланс состовляет: ", money, "монет") 

while money > 10:
    input("Нажмите ENTER чтобы начать ")
    play = input("Во что хотите сыграть? (кубик/рулетка) ") 


    if play == "кубик":
       player_name  = randint(1, 6)
       enemy_name  = randint(1, 6)
       print("игрок выбросил", player_name)
       print("компьютер выбросил", enemy_name)

       if player_name > enemy_name:
           money += 1000
           print(money)
           print("Вы победили")
       elif player_1 < player_2:
           money -= 1000
           print(money)
           print("Победил комьпьютер")
       else:
           print("ничья")
           print(money)                                                                                                                                                                                                                                          print(money                                                                                                                                                                                                                  money -= 10                                                                                                                                                                                                                                            print(mo                                                                                                                                                                                                                                            print("ни                                                                                                                                                                                                                                         print(money)
    elif play == "рулетка":
        color = randint(1, 2)
        stavka = input("на какой цвет хотите поставить? (красный/чёрный) ")
        if color == 1:
            print("красный")
            if  stavka == "красный":
                print("выпал красный")
                money += 1000
                print(money)
            elif stavka == "чёрный":
                money -= 1000
                print(money)
        elif color == 2:
            print("чёрный")
            if  stavka == "красный":
                money -= 1000
                print(money)
            elif stavka == "чёрный":
                print("выпал чёрный")
                money += 1000
                print(money)

    
