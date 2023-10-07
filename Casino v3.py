

from random import randint
money = 10000
print("Ваш баланс состовляет: ", money, "монет") 

while money > 999:
    input("Нажмите ENTER чтобы начать ")
    play = input("Во что хотите сыграть? (кубик/рулетка) ") 


    if play == "кубик":
        player_1 = randint(1, 6)
        player_2 = randint(1, 6)

        print("игрок выбросил", player_1 )
        print("компьютер выбросил", player_2 )

        if player_1 > player_2:
            money += 1000
            print(money)
            print("Вы победили")
        elif player_1 < player_2:
            money -= 1000
            print(money)
            print("Победил комьпьютер")
        else:
            print("ничья")
            print(money)

    elif play == "рулетка":
        color = randint(1, 2))
        stavka = input("на какой цвет хотите поставить? (красный/чёрный) ")
        if color == 1:
            print("красный")
            if  stavka == "красный":
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
                money += 1000
                print(money)
        print("выпал цвет", )

    










    
