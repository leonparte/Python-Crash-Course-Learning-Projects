# 定义函数

# 从一个简单的函数开始
print("\n-----------------------------------------\n")


def hello_world():
    """本函数用于输出一条‘hello world’"""
    print("Hello World!")


hello_world()

# 向函数传递信息
print("\n-----------------------------------------\n")


def welcome_msg(username):
    """本函数用于显示一条简单的问候语"""
    print("Welcome,", username + "!")


name = input("\nPlease enter the guest:\n").title()
welcome_msg(name)

print("\n-----------------------------------------\n")

