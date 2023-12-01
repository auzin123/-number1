hp = 100
player_hp = hp
money = input("Сколько денег зачислить? ")
print("У вас", money, "рублей")
print("ВОТ СПИСОК ВСЕХ ТОВАРОВ")
print("1 - Аптечка(восставновить все хп)")
print("2 - Доспехи(добавляет +50% жизней)")
print("3 - оберег()")
buy = input("Какой товар преобристи? ")
if buy == "1":
    if money > "99":
        player_hp = hp
        print("Теперь у вас", player_hp, "хп")
    elif money <= "100":
        print("Недостаточно денег")
if buy == "2":
    if money > "499":
        player_hp = hp * 1.5
        print("Теперь у вас", player_hp, "хп")
    elif money < "500":
        print("Недостаточно денег")