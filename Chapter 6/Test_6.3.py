# 遍历字典

player = {'name': 'Dwyane Wade', 'number': '3'}
fav_player = {'Ye': 'Wade', 'Tao': 'McGrady', 'Xie': 'Wade', 'Liu': 'Paker'}

# 遍历所有键-值对
print("\n-----------------------------------------\n")

for name, player_name in fav_player.items():
    print("\nname:" + name)
    print("player_name:" + player_name)


# 遍历字典中的所有键
print("\n-----------------------------------------\n")

# 遍历字典时，会默认遍历所有的键，因此，若下面的“fav_player.keys()”写成“fav_player”，没有实际影响
print("\nTest of using'fav_player':")
for name in fav_player:
    print(name.title())

print("Test of using'fav_player.keys()':")
for name in fav_player.keys():
    print(name.title())

# 按顺序遍历字典中的所有键
print("\n-----------------------------------------\n")

for name in sorted(fav_player.keys()):
    print(name.title())

# 遍历字典中所有的值
print("\n-----------------------------------------\n")

for fav_name in fav_player.values():
    print(fav_name.title())

print("\n-----------------------------------------\n")