from random import randint

player_name = input("Как вас зовут?")
player_level = 10
player_hp = 50 *player_level
player_expe = 0
money = 1000

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
        enemy_hp = 50 * enemy_level
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
                print(money, "монет")
                player_expe += enemy_level
                print(player_name, "получил", enemy_level, "опыта")
                if player_expe % 10 == 0:
                    player_level += player_expe // 10
                    player_expe += enemy_level % 10
                    print(player_name,"получил", player_level, "уровень")
                    player_hp / player_level
                break
            enemy_attack = randint(0, 10) + enemy_level
            player_hp -= enemy_attack
            print(enemy_name, "ударил", player_name, "на", enemy_attack, "жизней")
            print("У", player_name, "стало", player_hp, "жизней")
            if enemy_hp <= 0:
                print(enemy_name, "погиб")
                print("получает 25 монет")
                money += 25
                print(money, "монет")    
            break
                
        print("бой окончен")
    elif option == "2":
        print("игра окончена")
        break
    elif option == "3":
        while True:
            print("Вот список всех товаров")
            print("0 - уйти")
            print("1 - Восстановить все хп = 25 монет")
            buy = input("Что будем делать?")
            if buy == "0":
                break
            elif buy == "1":
                if money >= 25:
                    money -= 25
                    player_hp = 10 *player_level
                    print("у вас", player_hp, "хп")
                    print(money, "монет")
                    
    elif option == "4":
            while money > 0:
                play_activ = input("Будем играть или уйдём?")
                if play_activ == "играть":           
                    from random import randint
                    play = input("Во что хотите сыграть? (кубик/рулетка) ") 
                    bet = int(input("Сколько поставить?"))
                    if bet >= 1:
                        if play == "кубик":
                            player_1 = randint(1, 6)
                            player_2 = randint(1, 6)

                            print("игрок выбросил", player_1 )
                            print("компьютер выбросил", player_2 )

                            if player_1 > player_2:
                                money += bet * 2
                                print(money, "монет")
                                print("Вы победили")
                            elif player_1 < player_2:
                                money -= bet
                                print(money, "монет")
                                print("Победил комьпьютер")
                            else:
                                print("ничья")
                                print(money, "монет")

                        elif play == "рулетка":
                            color = randint(1, 2)
                            stavka = input("на какой цвет хотите поставить? (красный/чёрный) ")
                            if color == 1:
                                print("красный")
                                if  stavka == "красный":
                                    money += bet * 2
                                    print(money, "монет") 
                                elif stavka == "чёрный":
                                    money -= bet
                                    print(money, "монет")
                            elif color == 2:
                                print("чёрный")
                                if  stavka == "красный":
                                    money -= bet
                                    print(money, "монет")
                                elif stavka == "чёрный":
                                    money += bet * 2
                                    print(money, "монет")
                    else:
                        print("нету такого числа")       
                elif play_activ == "уйти":
                    break
