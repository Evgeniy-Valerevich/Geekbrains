number = int(input("Please, enter a number: "))
biggest_digit = 0
while number != 0:
    test_digit = number % 10
    if test_digit == 9:
        biggest_digit = test_digit
        break
    elif test_digit > biggest_digit:
        biggest_digit = test_digit
    number = number // 10
print(f"Biggest digit in your number is: {biggest_digit}")
