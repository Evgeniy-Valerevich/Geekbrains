number = int(input("Enter the number: "))
control = 0
digit = number % 10
number_1 = number // 10
while number_1 != 0:
    if digit > control:
        control = digit
    if control == 9:
        break
    digit = number_1 % 10
    number_1 = number_1 // 10
print(f"The biggist digit in your number: {control}")