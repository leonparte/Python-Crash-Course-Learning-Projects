import this as zen

filename = 'Zen_test_001.txt'
with open(filename, 'w') as file_object :
    file_object.write("".join([zen.d.get(c, c) for c in zen.s]))

# 这里将《Zen of Python》输出为txt文本是在阅读了"this.py"的内容的前提下实现的
# 下一步的目标是在不知道其内容的前提下实现将《Zen of Python》输出为txt文本
# author leonparte