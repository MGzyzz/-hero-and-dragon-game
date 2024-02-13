import random

dragon = {
    'hp': 2000,
    'defence': 120,
    'str': 150,
    'weapon': 110,
    # (150 + 0 ) - 100 = 50
}

hero = {
    'hp': 1000,
    'defence': 100,
    'str': 150,
    'weapon': 250,
    'shield': 150,
    'has_shield': False,
    'heal_potion': 3,
 
}


def modify_health(person, damage):
    person -= damage

    if person < 0:
        person = 0
        return person
    else:
        return person


def display_hero_info(hero):
    print(f"\n{'-' * 15} HERO {'-' * 14}\n")
    result = f'\n{"Name":<14}{"stats":>5}\n{"-" * 35}\n'

    for name in hero:
        stats_number = hero[name]
        result += f"{name.capitalize():<12} {stats_number:>5}\n"

    return print(result)


def display_dragon_info(dragon):
    print(f"\n{'-' * 13} DRAGON {'-' * 14}\n")
    result = f'\n{"Name":<12}{"stats":>5}\n{"-" * 35}\n'

    for name in dragon:
        stats_number = dragon[name]
        result += f"{name.capitalize():<10} {stats_number:>5}\n"

    return print(result)


def hero_attack():
    while dragon['hp'] > 0:
        print("===== ГЕРОЙ АТАКОВАЛ ДРАКОНА! =====\n")

        if 75 > random.randint(1, 100):
            damage_hero = (hero['str'] + hero["weapon"]) - dragon['defence']
            person = modify_health(dragon['hp'], damage_hero)
            dragon['hp'] = person
            print(f"\nДРАКОН ПОЛУЧИЛ УРОН В РАЗМЕРЕ: {damage_hero} ЕД \n\nЗДОРОВЬЕ ДРАКОНА: {dragon['hp']} HP \n")

            return dragon['hp']
        else:
            return print("\n===== ГЕРОЙ ПРОМАХНУЛСЯ: =====\n")


def fireball():
    if 50 > random.randint(1, 100):
        print("\nДРАКОН ГОТОВИТЬСЯ ПРИМЕНИТЬ ОГНЕННЫЙ ШАР!\n")
        return True
    else:
        return False


def dragon_attack():
    while hero['hp'] > 0:

        damage_dragon = (dragon['str'] + dragon['weapon']) - hero['defence']
        if hero['has_shield'] and fireball():
            damage_dragon = 0
            print("\nГЕРОЙ ОТРАЗИЛ ОГНЕННЫЙ ШАР\n")

        elif not hero['has_shield'] and fireball():
            fireball_damage = dragon['str'] * 2
            damage_dragon = fireball_damage
            print("\nДРАКОН ПУСТИЛ ОГНЕННЫЙ ШАР!\n")

        person = modify_health(hero["hp"], damage_dragon)
        hero['hp'] = person

        print(f"ДРАКОН АТАКОВАЛ ГЕРОЯ!\n\n===== ГЕРОЙ ПОЛУЧИЛ УРОН В РАЗМЕРЕ: {damage_dragon} =====\n")
        return hero['hp']


def equip_shield():
    if not hero['has_shield']:
        shield = hero['shield'] + hero['defence']
        hero['defence'] = shield
        hero['has_shield'] = True

        return hero['defence']


def remove_shield():
    if hero['has_shield']:
        hero_defence = hero['defence'] - hero['shield']
        hero['defence'] = hero_defence
        hero['has_shield'] = False

        return hero['defence']


def hero_pass():
    return print("\n===== ГЕРОЙ НЕ АТАКОВАЛ! =====\n")


def heal_potion():
    if hero['heal_potion'] == 0:
        return print("ЗЕЛЬЯ ЛЕЧЕНИЕ НЕ ОСТАЛОСЬ")

    else:
        heal = 500
        hero['hp'] += heal
        hero['heal_potion'] -= 1

        print(f" ===== ГЕРОЙ ПРИМЕНИЛ ЗЕЛЬЯ ЛЕЧЕНИЕ =====\n\n=====ЗДОРОВЬЕ ВОССТАНОВИЛОСЬ НА 500 ЕД! =====\n\nЗЕЛЬЕВ ЛЕЧЕНИЕ ОСТАЛОСЬ {hero['heal_potion']}\n")

        return hero['hp']


def turn_dragon():
    print("\n===== ХОД ДРАКОНА =====\n")
    random_choice = random.randint(1, 100)
    if random_choice > 50:
        dragon_attack()
    else:
        print("\nДРАКОН ПРОСПАЛ СВОЙ ХОД! \n")

    return print(f"\n===== ЗДОРОВЬЯ ГЕРОЯ: {hero['hp']} HP =====\n")


def turn_hero():
    print(
        "Добро пожаловать в игру. Ваша задача победить дракона, если вы не сможете одолеть дракона, то игра закончиться поражением игрока\nВыбор действий происходит с помощью индексов ниже\n")
    while True:
        if not dragon['hp'] == 0 and not hero['hp'] == 0:
            print("\n===== ХОД ГЕРОЯ! =====\n")
            hero_choose = input("Каково будет ваше действие?\n[1]атаковать\n[2]пропустить ход\n[3]поднять щит\n[4]Применить Зелья\n")

            match int(hero_choose):
                case 1:
                    hero_attack()
                case 2:
                    hero_pass()
                case 3:
                    print("\n===== ГЕРОЙ ЭКИПИРОВАЛ ЩИТ! =====\n")
                    equip_shield()
                case 4:
                    heal_potion()
                case _:
                    print("Неверная команда попробуйте еще раз")
                    turn_hero()

        elif hero['hp'] == 0:
            print("\n===== ПОБЕДИЛ ДРАКОН! =====\n")
            break
        elif dragon['hp'] == 0:
            print("\n===== ПОБЕДИЛ ГЕРОЙ! =====\n")
            break

        turn_dragon()
        remove_shield()
        display_hero_info(hero)
        display_dragon_info(dragon)

display_hero_info(hero)
display_dragon_info(dragon)
turn_hero()

