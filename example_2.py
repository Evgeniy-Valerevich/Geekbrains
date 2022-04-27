time = int(input("Please, enter a time in seconds: "))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f"You have entered: {hours:.0f} hours {minutes:.0f} minutes {seconds:.0f} seconds")
