# 使用列表的一部分

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen']

# 切片
print("\n-----------------------------------------\n")

# 注意[a:b]打印的是a,...,b-1
print("迈阿密的先发外线球员有：\n", players[0:4])
print("迈阿密的两位超巨是：\n", players[1:3])

# 如果[a,b]中的第一个索引（a）没有指定，则默认从列表开头开始；
# 类似的，没有指定第二个索引，则会默认到列表末尾停止：
print("迈阿密的先发后场为：\n", players[:2])
print("迈阿密的第六人为：\n", players[5:])

# 负索引可以表示列表的最后几个元素：
print("迈阿密终结比赛的一套阵容为：\n", players[-5:])


# 遍历切片
print("\n-----------------------------------------\n")

print("我最喜欢的两个迈阿密球员是：")
for player in players[1:3]:
    print(player.title())

# 复制列表
print("\n-----------------------------------------\n")

my_players = ["Yao Ming", "Dwyane Wade", "Stephen Curry", "Tracy McGrady", "Michael Jordan", "Kobe Bryant"]
my_bro_players = my_players[:]
# 若写成my_bro_players = my_players，则相当于将my_players赋给了my_bro_players，则实际上只有一个表
# 个人理解：这么做相当于仅仅使得my_bro_players的指针指向了my_players

print("My Favorite players are:")
print(my_players)

print("His Favorite players are:")
print(my_bro_players)

print("\n-----------------------------------------\n")