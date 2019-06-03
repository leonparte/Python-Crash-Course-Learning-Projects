# 导入类
from superstar import SuperStar

dwyane_wade = SuperStar('Dwyane Wade', 34, 'Miami Heat', 'Shooting guard')
dwyane_wade.set_year(14)
dwyane_wade.update_score(20000)
dwyane_wade.update_score(3000)
dwyane_wade.update_score(165)
dwyane_wade.set_NBA_titles(1, '2006')
dwyane_wade.update_NBA_titles('2012')
dwyane_wade.update_NBA_titles('2013')
print(dwyane_wade.get_description())