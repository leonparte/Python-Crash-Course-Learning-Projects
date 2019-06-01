# 使用while循环来处理列表和字典

# 在列表之间移动元素
print("\n-----------------------------------------\n")
print("在列表之间移动元素:")

ages = [17, 27, 24, 6, 18, 71, 19, 25, 33]
adult = []
minor = []

print(ages)

while ages:
    age = ages.pop()
    if age < 18:
        minor.append(age)
    else:
        adult.append(age)

print("adult", adult)
print("minor", minor)
print("ages", ages)

# 删除包含特定值的所有列表元素
print("\n-----------------------------------------\n")
print("删除包含特定值的所有列表元素:")

active_players = ['Dwyane Wade', 'Stephen Curry', 'Lebron James', 'Ray Allen', 'Shane Battier', 'Chris Bosh']
retired_players =["Shaquille O'Neal", 'Michael Jordan', 'Kobe Bryant']

while True:
    hello_msg = 'Please enter the name of retiring player or "q" to quit:'
    print(hello_msg)
    r_player = input().title()

    if r_player == 'Q':
        print("quit!")
        break
    elif r_player not in active_players:
        print(r_player, "is not an active player!\n")
    else:
        active_players.remove(r_player)
        retired_players.append(r_player)
        print('Now, active_players is', active_players)
        print('Now, retired_players is', retired_players)

# 使用用户输入来填充词典
print("\n-----------------------------------------\n")
print("使用用户输入来填充词典:")

fav_players = {}

while True:
    name = input("\nWhat's your name?\n").title()
    player = input("\nWhat is your favorite player's name?\n").title()

    fav_players[name] = player

    repeat = input("\nWould you want to end input? enter 'y' to end, enter else to continue.\n")
    if repeat.lower() == 'y':
        print("input ending!\n")
        break

for name, fav_player in fav_players.items():
    print(name + "'s favorite player is", fav_player + ".")

print("\n-----------------------------------------\n")