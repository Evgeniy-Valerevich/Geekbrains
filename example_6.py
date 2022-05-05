my_list = []
while True:
    my_dict = {}
    num = int(input("Please, enter a number of product: "))
    my_dict['Название'] = input('Please, enter the name "Название" of product: ')
    my_dict['Цена'] = input('Please, enter the price "Цена" of product: ')
    my_dict['Количество'] = input('Please, enter the quantity "Количество" of product: ')
    my_dict['ед.'] = input('Please, enter the unit of measurement "ед." of product: ')
    my_cort = (num, my_dict)
    my_list.append(my_cort)
    stop = input('Do you want to continue? Y/N: ')
    stop = stop.upper()[0]
    if stop == 'N':
        break
    elif stop != 'Y':
        print("incorrect input.")
        break
print(f"Your list is: \n {my_list}")
new_dict = {}
name_list = []
price_list = []
quantity_list = []
unit_list = []
for i in range(len(my_list)):
    q = my_list[i][1]
    name_list.append(q['Название'])
    price_list.append(q['Цена'])
    quantity_list.append(q['Количество'])
    unit_list.append(q['ед.'])
new_dict['Название'] = name_list
new_dict['Цена'] = price_list
new_dict['Количество'] = (quantity_list)
new_dict['ед.'] = list(set(unit_list))
print(f'Your dictionary is: \n {new_dict}')
