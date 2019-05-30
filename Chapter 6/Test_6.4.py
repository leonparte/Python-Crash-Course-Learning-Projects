# 嵌套

fav_player = {'Ye': 'Wade', 'Tao': 'McGrady', 'Xie': 'Wade', 'Liu': 'Paker'}

# 字典列表
print("\n-----------------------------------------\n")

player_1 = {'name': 'Dwyane Wade', 'number': '3', 'position': 'shooting guard'}
player_2 = {'name': 'Stephen', 'number': '30', 'position': 'point guard'}
player_3 = {'name': 'LeBron James', 'number': '23', 'position': 'small '}

players = [player_1, player_2, player_3]

# 显示前两个球员信息
for player in players[:2]:
    print(player)

# 显示一共有多少球员信息：
print("Total number of palyers is", str(len(players)))

# 字典中存储列表
print("\n-----------------------------------------\n")

fav_2_players = ['Dwyane Wade', 'Stephen Curry']
my_fav = {'name': 'Ye', 'players_name': fav_2_players}
print(my_fav)

# 在字典中存储字典
print("\n-----------------------------------------\n")

my_fav_players = {'name': 'YE', 'player_1': player_1, 'player_2': player_2}
for key,value in my_fav_players.items():
    print(key, ":", value)

print("\n-----------------------------------------\n")