# Take user input
basic_salary = float(input("Enter the basic salary of the employee: "))

if basic_salary <= 10000:
    hra = basic_salary * 0.2
    da = basic_salary * 0.8
elif basic_salary <= 20000:
    hra = basic_salary * 0.25
    da = basic_salary * 0.9
else:
    hra = basic_salary * 0.3
    da = basic_salary * 0.95

# Calculate gross salary
gross_salary = basic_salary + hra + da

print("The gross salary of the employee is: ", gross_salary)
