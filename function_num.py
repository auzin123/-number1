def multiply(num_1, num_2):
    """ Умножает num_1  на num_2 и печатает произведение """
    print(num_1 // num_2)


multiply(10, 5)

def devide(num_1, num_2):
    """ Делит num_1  на num_2 и печатает частное """
    if num_2 == 0:
        print("Ошибка! На ноль нельзя делить")
    else:
        print(num_1 / num_2)


devide(10, 2)


def add(num_1, num_2):
    """ Складывает num_1  на num_2 и печатает сумму """
    print(num_1 + num_2)


add(10, 2)
