# 传递实参

# 位置实参、关键字实参
print("\n-----------------------------------------\n")


def jersey(p_name, p_number):
    print(p_name + "'s jersey's number is", str(p_number), ".")


print("位置实参：")
jersey("Wade", 3)
jersey("Curry", 30)

print("\n关键字实参：")
jersey(p_number=23, p_name="Jordan")

# 默认值
print("\n-----------------------------------------\n")


def nationality(p_name, p_nation="China"):
    print(p_name + "'s nationality is", p_nation, ".")


nationality("Ye")

print("\n-----------------------------------------\n")