revenue = float(input("Please, enter revenue of your company: "))
costs = float(input("Please, enter costs of your company: "))
if revenue > costs:
    print(f'Excellent! Your company works with profit! Your company profitability is {(revenue / costs):.2f}')
    employees = int(input("Please, enter number of employees your company: "))
    print(f'Your company profitability on employee is {(revenue / costs / employees):.2f}')
elif revenue < costs:
    print(f'Terribly! Your company works with loss!')
else:
    print(f'Carefully! Your company works at zero!')
