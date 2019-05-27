# 从列表中删除元素

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen']

# 使用del语句删除元素
print("\n-----------------------------------------\n")

del players[-1]
print(' The starting lineup of Miami Heat are:\n', players)

# 使用方法pop()删除元素
print("\n-----------------------------------------\n")

players.append('Allen')
sixth_man = players.pop()
print("Miami's 6th man is", sixth_man, '.')

# 弹出列表中任何位置的元素
print("\n-----------------------------------------\n")

Runaway = players.pop(2)
print("The man who ran away after losing to the Spurs is", Runaway, ".")

# 根据值删除元素
print("\n-----------------------------------------\n")

players = ['Justise Winslow', 'Dion Waiters', 'Josh Richardson', 'Kelly Olynyk', 'Bam Adebayo', 'Dwyane Wade']
print("The players of Miami  who played in the game with the Warriors are :\n", players)
players.remove('Dwyane Wade')
print("These players will play for NBA next season:\n", players)

print("\n-----------------------------------------\n")

print("Damn it, I am fucking sad.")

print("\n-----------------------------------------\n")

# 以下为想到我韦退役从网上找的显示图片的代码，放了一张我韦的图片

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

lena = mpimg.imread('DWade.jpg') # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
lena.shape #(512, 512, 3)
plt.imshow(lena) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()

print("\n-----------------------------------------\n")