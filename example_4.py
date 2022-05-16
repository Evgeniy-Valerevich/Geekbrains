def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    x_2 = x
    for i in range(abs(y)-1):
        x_2 = x_2 * x
    return 1 / x_2


num_x = float(input("Please, enter a real number: "))
num_y = int(input("Please, enter a negative number: "))
if num_y >= 0:
    print(f"Number {num_y} isn't negative number")
else:
    print(f'The first way. Exponentiation {num_y} of a number {num_x} is {my_func_1(num_x, num_y)}')
    print(f'The second way. Exponentiation {num_y} of a number {num_x} is {my_func_2(num_x, num_y)}')
