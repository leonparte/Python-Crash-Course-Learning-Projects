# 使用字典

player = {'name': 'Dwyane Wade', 'number': '3'}

# 访问字典中的值
print("\n-----------------------------------------\n")

print("The number of", player['name']+"'s jersey is ", player['number'])

# 添加“键-值”对
print("\n-----------------------------------------\n")

player['position'] = 'shooting guard'
print(player)

# 先创建一个空字典
print("\n-----------------------------------------\n")

new_player = {}
new_player['name'] = 'LeBron James'
new_player['number'] = '6'

print(new_player)

# 修改字典中的值
print("\n-----------------------------------------\n")

print(new_player)
new_player['number'] = '23'
print(new_player)

# 删除“键-值”对
print("\n-----------------------------------------\n")

new_player['attr'] = 'Traitor'
print(new_player)
del new_player['attr']
print(new_player)

# 有类似对象组成的字典
print("\n-----------------------------------------\n")

fav_player = {'Ye': 'Wade', 'Tao': 'McGrady', 'Xie': 'Wade', 'Liu': 'Paker'}
print(fav_player['Tao'])

print("\n-----------------------------------------\n")
