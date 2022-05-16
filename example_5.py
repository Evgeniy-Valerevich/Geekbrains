def my_func(func_str):
    if 's' in func_str:
        ind = func_str.index('s')
        control_str = func_str[0:ind]
    else:
        control_str = func_str
    func_list = control_str.split()
    num_list = list(map(int, func_list))
    my_sum = 0
    for i in range(len(num_list)):
        my_sum += num_list[i]
    return my_sum


result = 0
while True:
    my_str = input("Please, enter numbers with space. Enter 's', if you want stop: ")
    result = result + my_func(my_str)
    print(f'Sum of your numbers is: {result}')
    if 's' in my_str:
        break
