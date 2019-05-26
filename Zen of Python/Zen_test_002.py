import sys
# 为了控制引入的this.py的输出，导入sys模块
# 关于sys模块，python文档是这么描述的：
# 该模块提供了一些变量和函数。这些变量可能被解释器使用，也可能由解释器提供。
# 这些函数会影响解释器。本模块总是可用的。

print("\n\n------------------------------------\n\n")

output = sys.stdout

# 功能：stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象.
# 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的.
# 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ),
# 或者以非标准的方式处理它们

filename = 'Zen_test_002.txt'
outputfile = open(filename, 'w')
sys.stdout = outputfile

import this

outputfile.close()
sys.stdout = output

# 将系统输出换回原来的方式

print("完成输出！")

print("\n\n------------------------------------\n\n")


# 这里实现了仅仅知道this.py可以输出“Zen of python”，
# 而不知道其具体内容，就将其输出为文档的目标
# 问题：在代码中间进行import，而不知道如何实现在代码上方import，
# 中间再调用