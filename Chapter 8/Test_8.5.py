# 传递任意数量的实参


# 从一个例子开始
print("\n-----------------------------------------\n")


def buy_foods(*foods):
    """打印需要购买的食品清单"""
    print('The foods that need buy are', foods)


buy_foods('巧克力', '冰激凌', '可乐')

# 结合使用位置实参和任意数量实参
print("\n-----------------------------------------\n")


# p_l_e:personal learning experience
def p_l_e(name, *schools):
    print(name.title(), "had studied in such schools:\n", schools)


p_l_e('Ye haopin', 'huanfeng primary school', 'no.2 middel school of chaohu ', 'no.1 middel school of chaohu ',
      'SUFE', 'NUFE')

# 使用任意数量的关键字实参
print("\n-----------------------------------------\n")


def bulid_profile(name, **user_info):
    profile = {}
    profile['name'] = name
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = bulid_profile('Tao Yuchen', country='China', age=24, sex='male')
print(user_profile)

print("\n-----------------------------------------\n")