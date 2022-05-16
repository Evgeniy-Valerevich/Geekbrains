def my_func(num_1, num_2, num_3):
    my_list = [num_1] + [num_2] + [num_3]
    big_1 = max(my_list)
    my_list.remove(big_1)
    big_2 = max(my_list)
    return big_1 + big_2


my_num_1 = float(input("Please, enter first number: "))
my_num_2 = float(input("Please, enter second number: "))
my_num_3 = float(input("Please, enter third number: "))
print(f'The sum of the two largest numbers is {my_func(my_num_1, my_num_2, my_num_3)}')
