my_list = [[1, 2, True], "True", False, 13.13, (1, "good", 2), 2, None]
for i, el in enumerate(my_list, 1):
    print(f"{i}. {type(el)}")
