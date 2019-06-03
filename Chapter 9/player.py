# 使用类和实例
class Player():
    """描述一名篮球运动员"""

    def __init__(self, name, age, team, positoin):
        """初始化描述运动员的属性"""
        self.name = name
        self.age = age
        self.team = team
        self.positon = positoin
        self.year = 0
        self.score = 0

    def get_description(self):
        string = self.name + ', who is ' + str(self.age) + ' years old, has played for ' + \
                 self.team + ' as a ' + self.positon + ' for ' + str(self.year) + ' years.\n' + \
                 'He has scoring ' + str(self.score) + ' points in NBA.\n'
        return string

    def set_year(self, years):
        """设置职业生涯年数"""
        self.year = years

    def update_score(self, score):
        """更新生涯总得分"""
        self.score += score

    def update_year(self):
        """更新生涯年数"""
        self.year += 1
        self.age += 1


dwyane_wade = Player('Dwyane Wade', 34, 'Miami Heat', 'Shooting guard')
dwyane_wade.set_year(14)
dwyane_wade.update_score(20000)
dwyane_wade.update_score(3000)
dwyane_wade.update_score(165)
print(dwyane_wade.get_description())