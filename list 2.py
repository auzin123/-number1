from random import choice


def get_hero(
        name=None,
        hp=100,
        level=1,
        xp=0, 
        money=25, 
        inventory=" "
        ) -> list:
    """ Возвращает список - героя """
    if not name:
        names = ("Роман", "Валера", "Акакий", "Мао")
        name = choice(names)
    if not inventory:
        inventory = None
    return [name, hp, level, xp, money, inventory]

def show_hero(hero: list) -> None:
    """ Выводит на экран характеристики героя """
    print("-" * 15)
    print("Имя:", hero[0])
    print("Здоровье:", hero[1])
    print("Уровень:", hero[2])
    print("Опыт:", hero[3])
    print("Деньги:", hero[4])
    print("Инвентарь:", hero[5])
    print("-" * 15)


def visit_shop(hero: list, shop_items: list):
    """ Выводит на экран текст магазина """
    """ Выводит на экран пронумерованные опции """
    """ Предлагает герою выбор опции """
    """ Работает по выбранной опции """
    show_hero(player)
    print(f"{hero[0]} прихал в лавку.")
    price = 10
    print("Распродажа: все товары по 10 монет")
    print("1 - Купить товары")
    print("2 - Продать товары")
    print("3 - Выйти из лавки")
    print("-" * 15)
    option = input("Введите номер опиции: ")
    if option == "1":
        for num, item in enumerate(shop_items, 1):
            print(f"{num} - {item}")
        print("0 -  Отмена")
        print("-" * 15)
        option = input("Введите номер товара: ")
        print("-" * 15)
        if int(option) > len(shop_items) or int(option) < 0:
            print("неверная опция")
        elif option == "0":
            print("вы вышли")
        else:
            if hero[4] < price:
                print(f"у {hero[0]} недостаточно денег")
            else:
                hero[4] -= price
                hero[5].append(option) - 1
                print(f"{hero[0]} купил {shop_items[int(option) - 1]} и теперь у него {hero[4]} денег")
                print("-" * 15)
        
        
player = get_hero()
shop_items = ["зелье лечения", "новое оружие", "зелье копчения",]
visit_shop(player, shop_items)