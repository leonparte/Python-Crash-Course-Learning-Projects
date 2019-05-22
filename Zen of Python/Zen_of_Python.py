import this as zen

filename = 'zen_of_Python.txt'
fileadress = zen
print('\n\ntest',fileadress,'\n\n')

with open(filename, 'w') as file_object :
    f = open("D:\Program Files\Anaconda3\lib\\this.py","r")
    lines = f.readlines()  # 调用文件的 readline()方法
    for line in lines :
        print(line)
        file_object.write(line)

    f.close()

print('\n',filename)