file_1 = 'input_test_1.txt'
file_2 = 'input_test_2.txt'
file_3 = 'input_test_3.txt'
filenames = [file_1, file_2, file_3]

for filename in filenames:
    try:
        with open(filename, 'w') as file_object:
            file_object.write('I love Python!\nI love Java!')
    except FileNotFoundError:
        msg = 'Sorry, the file named ' + filename + ' does not exist.'
        print(msg)

print("\n-----------------------------------------\n")

with open(file_1, 'w') as file_object:
    file_object.write('I love Java!')

with open(file_1, 'r') as file_object:
    contents = file_object.read()
    print("Show the effect of model 'w':\n", contents)

print("\n-----------------------------------------\n")

with open(file_2, 'a') as file_object:
    file_object.write('I love Java!')

with open(file_2, 'r') as file_object:
    contents = file_object.read()
    print("Show the effect of model 'a':\n", contents)

print("\n-----------------------------------------\n")

with open(file_3, 'r+') as file_object:
    file_object.write('I love Java!')

with open(file_3, 'r') as file_object:
    contents = file_object.read()
    print("Show the effect of model 'r+':\n", contents)

print("\n-----------------------------------------\n")