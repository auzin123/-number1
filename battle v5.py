import os
from random import randint


def game():
    player_name = input("Как вас зовут? ")
    player_level = 10
    player_hp = 50 * player_level
    player_expe = 0
    player_money = 1000
    visit_rock(player_name, player_hp, player_money, player_expe, player_level)


def visit_rock(player_name, player_hp, player_money, player_expe, player_level, ):
    os.system("cls")
    print("_________________________")
    print("1 = начать игру")
    print("2 = уйти")
    print("3 = пойти в магазин")
    print("4 = сыграть в казино")
    print("_________________________")
    option = input("Введите номер ответа и нажмите ENTER ")
    if option == "1":
        while True:
                enemy_name = ("GP_228")
                enemy_level = 10
                enemy_hp = 50 * enemy_level
                print(player_name, "сразится проитив", enemy_name)
                while True:
                    input("Нажмите ENTER чтобы атаковать ")
                    player_attack = randint(0, 10) + player_level 
                    
                    enemy_hp -= player_attack
                    print(player_name, "ударил", enemy_name, "на", player_attack, "жизней")
                    print("У", enemy_name, "стало", enemy_hp, "жизней")
                    if player_hp <= 0:
                        print(player_name, "победил!")
                        player_money += 25
                        print(player_money, "монет")
                        player_expe += enemy_level
                        print(player_name, "получил", enemy_level, "опыта")
                        if player_expe % 10 == 0:
                            player_level += player_expe // 10
                            player_expe += enemy_level % 10
                            print(player_name, "получил", player_level, "уровень")
                            player_hp / player_level
                        break
                    enemy_attack = randint(0, 10) + enemy_level
                    player_hp -= enemy_attack
                    print(enemy_name, "ударил", player_name, "на", enemy_attack, "жизней")
                    print("У", player_name, "стало", player_hp, "жизней")
                    if enemy_hp <= 0:
                        print(enemy_name, "погиб")
                        print("получает 25 монет")
                        player_money += 25
                        print(player_money, "монет")    
                    break        
                print("бой окончен")        
    elif option == "2":
        pass
    elif option == "3":
        while True:
            print("Вот список всех товаров")
            print("0 - уйти")
            print("1 - Восстановить все хп = 25 монет")
            buy = input("Что будем делать?")
            if buy == "0":
                break
            elif buy == "1":
                if player_money >= 25:
                    player_money -= 25
                    player_hp = 10 * player_level
                    print("у вас", player_hp, "хп")
                    print(player_money, "монет")
                    
    elif option == "4":
        while player_money > 0:
                print("_________________________")
                print("1 = будем")
                print("2 = уйти")                     
                print("_________________________")
                play_activ = input("Будем играть или уйдём?")
                if play_activ == "1":           
                    from random import randint
                    print("_________________________")
                    print("1 = сыграть в кубик")
                    print("2 = сыграть в рулетку")
                    print("3 = уйти")                     
                    print("_________________________")
                    play = input("Во что хотите сыграть?") 
                    bet = int(input("Сколько поставить?"))
                    if bet >= 1:
                        if play == "1":
                            player_1 = randint(1, 6)
                            player_2 = randint(1, 6)

                            print("игрок выбросил", player_1 )
                            print("компьютер выбросил", player_2 )

                            if player_1 > player_2:
                                player_money += bet * 2
                                print(player_money, "монет")
                                print("Вы победили")
                            elif player_1 < player_2:
                                player_money -= bet
                                print(player_money, "монет")
                                print("Победил комьпьютер")
                            else:
                                print("ничья")
                                print(player_money, "монет")

                        elif play == "2":
                            color = randint(1, 2)
                            stavka = input("на какой цвет хотите поставить? (красный/чёрный) ")
                            if color == 1:
                                print("красный")
                                if  stavka == "красный":
                                    player_money += bet * 2
                                elif stavka == "чёрный":
                                    player_money -= bet
                                    print(player_money, "монет")
                            elif color == 2:
                                print("чёрный")
                                if  stavka == "красный":
                                    player_money -= bet
                                    print(player_money, "монет")
                                elif stavka == "чёрный":
                                    player_money += bet * 2
                                    print(player_money, "монет")
                        elif play == "3":
                            break
                    else:
                        print("нету такого числа")       
                elif play_activ == "2":
                    break
game()