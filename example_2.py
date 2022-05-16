def personal_data(name, surname, birth_year, city, email, phone_number):
    print(f'Your name: {name}; Your surname: {surname}; Your birth year: {birth_year}; Your city: {city};'
          f'Your email: {email}; Your phone number: {phone_number}')


my_name = input("Please, enter your name: ")
my_surname = input("Please, enter your surname: ")
my_birth_year = input("Please, enter your birth year: ")
my_city = input("Please, enter your city: ")
my_email = input("Please, enter your email: ")
my_phone_number = input("Please, enter your phone number: ")
personal_data(name=my_name, surname=my_surname, birth_year=my_birth_year, city=my_city, email=my_email,
              phone_number=my_phone_number)
