a = float(input("Enter the distance: "))
b = float(input("enter the desired distance: "))
day = 1
while a < b:
    a = a * 1.1
    day += 1
if day > 1:
    print(f"the athlete will reach the desired distance in {day} days")
else:
    print("the athlete has achieved the desired result")
