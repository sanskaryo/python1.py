def check_odd_even():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_odd_even())