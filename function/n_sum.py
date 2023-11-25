
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

a = int(input("enter the number "))
print(sum_of_natural_numbers(a))

def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(sum_of_natural_numbers(10))



