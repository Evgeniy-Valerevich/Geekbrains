revenue = int(input("Enter revenue your business: "))
costs = int(input("Enter costs your business: "))
if revenue == costs:
    print("your business is running at zero!:|")
elif revenue > costs:
    print("your business is working for profit!:)")
    profit = ((revenue - costs) / revenue) * 100
    print(f"profitability of your business is {profit:.0f}%")
    person = int(input("Enter the number of employees in your business: "))
    person_profit = (revenue - costs) / person
    print(f"the company's profit per employee is {person_profit:.2f}")
else:
    print("your business is running at a loss!:(")
