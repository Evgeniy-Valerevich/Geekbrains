time = int(input('Enter the time in seconds: '))
hours = time // 3600
seconds = time % 60
minutes = (time % 3600) // 60
print(f'Time: {hours}:{minutes}:{seconds}')