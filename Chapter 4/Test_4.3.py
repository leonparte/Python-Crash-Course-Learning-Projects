# 创建数字列表

# 使用函数range()
print("\n-----------------------------------------\n")

print("The ages that I wasted a lot of time at are:")

# 注意，这里只会打印到24！
for age in range(19, 25):
    print(age)

# 使用rang()创建数字列表
print("\n-----------------------------------------\n")

# 若写成“ints = range(1,18)”,则print(ints)的结果即为：range(1,18)
ints = list(range(1, 18))
# 平方列表：
squares = []

print(ints)

# range(0, 18, 2):从0开始，不断加2，直到达到或超越终值（17）：
even_num = list(range(0, 18, 2))
print("\n0到17内的偶数有：\n", even_num)

for i in ints:
    squares.append(i**2)

print("\n1到17的平方为：\n", squares)

# 对数字列表执行简单的统计计算
print("\n-----------------------------------------\n")

test = [1, 12, 17, 19, 23, 3, 7, 6, 9, 11]

mi = min(test)
ma = max(test)
s = sum(test)

print("test列表内容如下：", test)
print("test列表中最小的数字为:", mi)
print("test列表中最大的数字为:", ma)
print("test列表中的数字之和为:", s)

# 列表解析
print("\n-----------------------------------------\n")

# 描述性列表名 = [ 函数表达式 for循坏]
# 注意这里的for循环没有冒号
cube = [num**3 for num in range(1, 18)]
print(cube)

print("\n-----------------------------------------\n")