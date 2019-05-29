# 条件测试

players = ['Chalmers', 'Wade', 'James', 'Battier', 'Bosh', 'Allen']
car = 'Chery'
ages = [17, 27, 24, 6, 18, 71, 19, 25, 33]

# 检查是否相等
print("\n-----------------------------------------\n")

print("Is his car Chery?\n", car.lower() == 'chery')
print("\nIs his car Audi?\n", car.lower() == 'audi')

# 检查是否相等时不考虑大小写
print("\n-----------------------------------------\n")

print("Is 'A == a' true in Python?\n", 'A' == 'a')
print("Is 'A.lower() == a' true in Python?\n", "A".lower() == 'a')

# 检查是否不相等
print("\n-----------------------------------------\n")

sex = "male"

if sex.lower() != "male":
    print("She is a lady!")
else:
    print("He is a man!")


#  比较数字
print("\n-----------------------------------------\n")


for age in ages:
    if age < 12:
        print("He is a child!")
    elif age < 18:
        print("He is a teenager!")
    elif age == 18:
        print("He is just become an adult!")
    else:
        print("He is an adult!")

#  检查多个条件
print("\n-----------------------------------------\n")

# 测试and：
for age in ages:
    if age < 12:
        print("He is a child!")
    elif 12 <= age and age < 18:
        print("He is a teenager!")
    elif age > 18:
        print("He is an adult!")
print("\n")

# 测试OR:
for age in ages:
    if age < 12 or age >= 60:
        print("your age is", age, ", you can visit the view free!")
    elif age >= 12 and age < 18:
        print("your age is", age, ", you can visit the view by half-price!")
    else:
        print("your age is", age, ", you should pay the full price!!")

# 检查特定值是否包含在列表中
print("\n-----------------------------------------\n")

test_name = 'Leon'

if test_name not in players:
    print(test_name.title() + ", you're not a Miami player.\n")

if "wade".title() in players:
    print("wade".title(), "is a Miami player!\n")

print("\n-----------------------------------------\n")