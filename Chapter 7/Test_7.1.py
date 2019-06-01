# 函数input()的工作原理

# 从对函数input()的简单使用开始
print("\n-----------------------------------------\n")

message = input("Tell me your favorite player:")
print(message)

# 编写清晰的程序
print("\n-----------------------------------------\n")

print("What is your name?")
name = input()
print("You are", name.title())

# 使用int()来获取数值输入
print("\n-----------------------------------------\n")

print("How od are you?")
age = int(input())
if age <= 12:
    print("You can visit the view for free!\n")
elif age <= 18:
    print("You can buy a ticket buy half-cut!\n")
else:
    print("You should buy tickets with full price!\n")

# 求模运算符
print("\n-----------------------------------------\n")

print("Please enter an integer:")
number = int(input())
if number % 2 == 0:
    print('The number you enter is', number, 'and it is even!')
else:
    print('The number you enter is', number, 'and it is odd!')

print("\n-----------------------------------------\n")