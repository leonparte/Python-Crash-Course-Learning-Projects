def count_words(filename):
    try:
        with open(filename, 'rb') as f_obj:
        # with open(filename, encoding='gb18030', errors='ignore') as f_obj:亦可实现
        # 但with open(filename) as f_obj:会报错，显示无法解码，这里的原因我尚未明白
        # 使用网上的这两种方法的影响我也尚不清楚
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file named ' + filename + ' does not exist.'
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print('The file "' + filename + '" has about ' + str(num_words) + ' words.')


filenames = [
    'A Study in Scarlet.txt',
    'The Hound of the Baskervilles.txt',
    'The Sign of the Four.txt',
    'The Valley of Fear.txt',
    'Detective Conan.txt'
]
for filename in filenames:
    count_words(filename)
