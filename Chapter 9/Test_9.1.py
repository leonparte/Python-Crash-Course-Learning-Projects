# 创建和使用类

class worker():

    def __init__(self, name, age):
        """初始化name和age"""
        self.name = name
        self.age = age

    def work(self):
        """工作去"""
        print(self.name.title() + '辛苦搬砖去啦！\n')

    def sleep(self):
        """干活太辛苦，休息"""
        print(self.name.title() + '觉得干活太辛苦了，他要休息去！\n')

me = worker('Leon', 25)
bro_1 = worker('Tao', 24)

bro_1.work()
me.sleep()