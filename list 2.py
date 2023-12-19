from random import choice


def get_hero(
        name=None,
        hp=100,
        level=1,
        xp=0, 
        money=25, 
        inventory="пусто"
        ) -> list:
    """ Возвращает список - героя """
    if not name:
        names = ("Роман", "Валера", "Акакий", "Мао")
        name = choice(names)
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


def visit_shop(hero, shop_items):
    """ Выводит на экран текст магазина """
    """ Выводит на экран пронумерованные опции """
    """ Предлагает герою выбор опции """
    """ Работает по выбранной опции """
    show_hero(player)
    print(f"{hero[0]} прихал в лавку.")
    print("1 - Купить товары")
    print("2 - Продать товары")
    print("3 - Выйти из лавки")
    print("-" * 15)
    option = input("Введите номер опиции: ")
    if option == "1":
        for num, item in enumerate(shop_items, 1):
            print(f"{num} - {item}")
        option = input("Введите номер товара чтобы его купить или введите 0 для отмены")
        # TODO: купить товар по выбранной опции
        


player = get_hero()
shop_items = ["зелье лечения", "зелье лечения", "зелье копчения",]
visit_shop(player, shop_items)
