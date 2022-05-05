my_list = ['January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December']
my_dict = {'January': "Winter", 'February': "Winter", 'March': "Spring", 'April': "Spring",
           'May': "Spring", 'June': "Summer", 'July': "Summer", 'August': "Summer",
           'September': "Autumn", 'October': "Autumn", 'November': "Autumn", 'December': "Winter"}
num = int(input("Please, enter a number of month: "))
month = my_list[num-1]
season = my_dict[month]
print(f'Your month is {month}. Season of your month is {season}')
