# 在列表中添加元素

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh']

print("\n-----------------------------------------\n")

print(players)

# 在列表末尾添加元素：
players.append('Allen')
print("Miami's 6th man is", players[5], '.')

del players[-1]

# 在指定位置插入元素
players.insert(5, 'Allen')
print(players)


print("\n-----------------------------------------\n")