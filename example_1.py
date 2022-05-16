def my_func(divisible, divisor):
    try:
        quotient = divisible / divisor
    except ZeroDivisionError:
        print('You entered zero. Division by zero is not possible')
        return
    return quotient


num_1 = float(input('Please, enter a divisible: '))
num_2 = float(input('Please, enter a divisor: '))
my_quotient = my_func(num_1, num_2)
print(f'{my_quotient:.2f} The quotient of dividing the divisible {num_1} by the divisor {num_2}')
