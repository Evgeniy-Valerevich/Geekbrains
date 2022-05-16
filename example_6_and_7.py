def int_func(func_str):
    return func_str.title()


my_str = input('Please, enter the words in lowercase: ')
print(f'Your words with the first letters in uppercase: {int_func(my_str)}')
