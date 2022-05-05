my_list = [7, 5, 3, 3, 2]
num = None
print(f"First rating: {my_list}")
while True:
    num = int(input("Please, enter rating element, if you want stop it - enter '-1': "))
    if num == -1:
        break
    for i in range(len(my_list)):
        control = len(my_list)
        if i == 0 and num > my_list[i]:
            my_list.insert(0, num)
        elif num <= my_list[i] and i == len(my_list)-1:
            my_list.append(num)
        elif num <= my_list[i] and num > my_list[i+1]: #купировал warning предыдущим условием
            my_list.insert(i+1, num)
        if control != len(my_list):
            break
    print(f"New rating with your rating element: {my_list}")
