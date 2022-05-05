string = input("Please, enter your string with spaces between words: ")
my_list = string.split()
for i, el in enumerate(my_list, 1):
    print(f"{i}. {el[:10]}")
