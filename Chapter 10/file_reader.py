file_path = 'D:\Program Files\Python_Test\Test\Learning Python\Zen of Python\Zen_test_001.txt '

with open(file_path) as file_object:
    lines = file_object.readlines()

length = 0
for line in lines:
    print(line.rstrip())
    length += len(line)

print(length)