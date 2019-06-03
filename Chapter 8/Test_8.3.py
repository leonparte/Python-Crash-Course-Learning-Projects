# 返回值

# 返回简单值
print("\n-----------------------------------------\n")


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


names = get_formatted_name('Ye', 'haopin')
print(names)

# 让实参变成可选的&返回字典&结合使用函数和while循环
print("\n-----------------------------------------\n")

fav_players = []


def fav_player(name, age, player=''):
    """返回最喜欢球员的姓名"""
    if player:
        fav_p = {'name': name, 'age': age, 'player': player}
    else:
        fav_p = {'name': name, 'age': age, 'player': 'Michael Jordan'}

    return fav_p


while True:
    q = input("\nWould you want to quit? Enter 'q' to quit,or enter else to continue.\n")
    if q.lower() == 'q':
        print('Quit!')
        break
    else:
        name = input("\nPlease enter your name:\n").title()
        age = int(input("\nPlease enter your age:\n"))
        f_p = input("\nPlease enter your favorite player, if he is Michael Jordan, "
                    "enter 'm' to continue:\n").title()
        if f_p == 'M':
            fav_players.append(fav_player(name, age))
        else:
            fav_players.append(fav_player(name, age, f_p))

print("\n")
for fav_player in fav_players:
    print(fav_player)

print("\n-----------------------------------------\n")