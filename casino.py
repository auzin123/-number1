
from random import randint
money = 10000
print("денег", money)

while money > 999:
    input("Нажмите ENTER чтобы сыграть")
    player_1 = randint(2, 12)
    player_2 = randint(2, 12)

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
print(money)


