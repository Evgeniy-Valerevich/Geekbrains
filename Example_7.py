start_result = float(input("Please, enter a start result of sportsman in meters: "))
finish_result = float(input("Please, enter a finish result of sportsman in meters: "))
day = 1
if start_result >= finish_result:
    print(f'Sportsman has reached the final result at first day')
else:
    while start_result < finish_result:
        day += 1
        start_result = start_result * 1.1
    print(f"Sportsman has reached the final result at least {finish_result} meters at {day} day")
