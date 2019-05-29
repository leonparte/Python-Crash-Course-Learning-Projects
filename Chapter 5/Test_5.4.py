# 使用if语句处理列表

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen', ]
active_players = ['Curry', 'James', 'leonard', 'Chalmers']

# 检查特殊元素
print("\n-----------------------------------------\n")

for player in players:
    print("\nYes,", player.title(), "played for Miami Heat and win the NBA title!")
    if player.title() == 'Wade':
        print("Dwyane Wade is the greatest player in Miami!")

# 确定列表是否为空
print("\n-----------------------------------------\n")

new_list = []

if new_list:
    print(new_list)
else:
    print("The list was empty!\n")

# 使用多个列表
print("\n-----------------------------------------\n")

for player in players:
    if player in active_players:
        print(player.title(), "is still play basketball in NBA!")
    else:
        print(player.title(), "has retired!")

print("\n-----------------------------------------\n")
