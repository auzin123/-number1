from random import randint

player_name = input("Как вас зовут?")
player_level = 5
player_hp = 100 *player_level
player_expe = 10


enemy_name =("GP_228")
enemy_level = 5
enemy_hp = 100 * enemy_level
enemy_expe = 10
print(player_name, "сразится проитив", enemy_name)
while True:
    input("Нажмите ENTER чтобы атаковать ")
    player_attack = randint(0, 10) * player_level 
       
    enemy_hp -= player_attack
    print(player_name, "ударил", enemy_name, "на", player_attack, "жизней")
    print("У", enemy_name, "стало", enemy_hp, "жизней")
    if player_hp <= 0:
        print(player_name, "погиб")
        player_expe += enemy_level
        print("+", enemy_expe, "опыта")
        break
    
    enemy_attack = randint(0, 10) * enemy_level
    player_hp -= enemy_attack
    print(enemy_name, "ударил", player_name, "на", enemy_attack, "жизней")
    print("У", player_name, "стало", player_hp, "жизней")
    if enemy_hp <= 0:
        print(enemy_name, "погиб")
        enemy_name += player_level
        print("+", player_expe, "опыта")
        break
print("бой окончен")

    
