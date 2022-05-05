my_list = []
new_list = []
n_el = int(input("Please, enter numbers of list's elements: "))
for i in range(n_el):
    el = input(f"Please, enter elements {i + 1}.:")
    my_list.append(el)
print(f"Your start list: {my_list}")
new_list = my_list
if n_el % 2 == 0:
    for i in range(len(new_list))[::2]:
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
else:
    for i in range(len(new_list) - 1)[::2]:
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
# print(f"Your start list: {my_list}") # вывод my_list на данном этапе возвращает значения new_list, не понимаю почему.
print(f"Your new list: {new_list}")
