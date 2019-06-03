# 传递列表

import time

# 从一个简单的应用开始
print("\n-----------------------------------------\n")

persons = []


def greeter(p_message):
    for p in p_message:
        name = p['name']
        print("Hello,", name.title() + "!")


def input_message(p_s):
    while True:
        name = input("\nPlease enter your name, or enter 'e' to end input:\n").title()
        if name == 'E':
            print("Input ending!\n")
            break
        else:
            age = int(input("\nPlease enter your age:\n"))
            person = {'name': name, 'age': age}
            p_s.append(person)


input_message(persons)
greeter(persons)

# 在函数中修改列表
print("\n-----------------------------------------\n")

print("在函数中修改列表:\n")


# 该函数输出一条生日祝福，并将过生日的人的年龄增加一岁
def birthday(persons):
    flag = True
    name = input("\nPlease enter the name of whose birthday is today, "
                 "or you can enter 'e' to end this function:\n").title()
    for person in persons:
        if name == 'E':
            print('omit this function!')
            flag = False
            break
        elif name == person['name']:
            print("\nHappy Birthday!\n", name, "\n")
            person['age'] += 1
            flag = False
        else:
            continue

    if flag:
        print("The name you entered is not in the list!\n")
        time.sleep(2)


birthday(persons)
for person in persons:
    print(person)

# 禁止函数修改列表
print("\n-----------------------------------------\n")

print("禁止函数修改列表")

# ns：names; n:name
def hello(ns):
    i = 0
    for n in ns:
        n = n.title()
        ns[i] = n
        print('hello,', n + '.')
        i += 1

    print(ns)


names = ['ye haopin', 'tao yuchen', 'xie zhigang', 'liu yisi']
hello(names[:])
print(names)

# 以上测试可以实现对原列表内容的保护，但下面的语句却不可以实现：
p = persons[:]
birthday(p)
for person in persons:
    print(person)

print("\n-----------------------------------------\n")