# 组织列表

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen']

# 使用方法sorted()对列表进行临时性排序
print("\n-----------------------------------------\n")

print("\nHere is the original lineup :\n", players)
print("\nHere is the sorted lineup :\n", sorted(players))
print("\nHere is the original lineup again:\n", players)

# 倒序打印列表
print("\n-----------------------------------------\n")

print("\nHere is the original lineup :\n", players)
players.reverse()
print("\nHere is the reverse lineup :\n", players)
players.reverse()

# 使用sort()方法对列表进行永久性排序
print("\n-----------------------------------------\n")

print("\nHere is the original lineup :\n", players)
players.sort()
print("\nHere is the sort lineup :\n", players)

# 确定列表长度
print("\n-----------------------------------------\n")

length = len(players)
print("The length of the list 'players' is:", length)

print("\n-----------------------------------------\n")