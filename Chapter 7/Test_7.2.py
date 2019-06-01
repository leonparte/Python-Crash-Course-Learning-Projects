# while循环简介

# 使用while循环
print("\n-----------------------------------------\n")

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen']
i = 0
while i < 6:
    print(players[i])
    i += 1

# 让用户选择何时退出
print("\n-----------------------------------------\n")

print("让用户选择何时退出")
fav_players = []
hello_msg = "Welcome! Please enter your favorite player or 'q' to quit!"
input_msg = ""
while input_msg != 'q':
    print(hello_msg)
    input_msg = input()
    if input_msg != 'q':
        fav_players.append(input_msg.title())
        print("Now, you fav_players is:", fav_players)
    else:
        print("quit!".title())

# 使用标志
print("\n-----------------------------------------\n")

print("使用标志")
fav_players = []
hello_msg = "Welcome! Please enter your favorite player or 'q' to quit!"
input_msg = ""
flag = True
while flag:
    print(hello_msg)
    input_msg = input()
    if input_msg != 'q':
        fav_players.append(input_msg.title())
        print("Now, you fav_players is:", fav_players)
    else:
        flag = False
        print("quit!".title())


# 使用break退出循环
print("\n-----------------------------------------\n")
print("使用break退出循环：")

fav_players = []
hello_msg = "Welcome! Please enter your favorite player or 'q' to quit!"
input_msg = ""
while True:
    print(hello_msg)
    input_msg = input()
    if input_msg != 'q':
        fav_players.append(input_msg.title())
        print("Now, you fav_players is:", fav_players)
    else:
        print("quit!".title())
        break

# 在循环中使用continue
print("\n-----------------------------------------\n")
print("在循环中使用continue：")

fav_players = []
hello_msg = "Welcome! Please enter your favorite player or 'q' to quit!"
input_msg = ""
while True:
    print(hello_msg)
    input_msg = input()
    if input_msg != 'q':
        fav_player = input_msg.title()
        if fav_player in fav_players:
            print("He is already in the list, your fav_players is:", fav_players)
            continue
        fav_players.append(fav_player)
        print("Now, your fav_players is:", fav_players)
    else:
        print("quit!".title())
        break

print("\n-----------------------------------------\n")