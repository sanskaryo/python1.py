start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_even = 0
sum_odd  = 0

for num in range(start, end +1):
    if num % 2 ==0:
        sum_even += num
    else:
        sum_odd += num
        
        print(f"Sum of even numbers between {start} and {end}: {sum_even}")

print(f"Sum of odd numbers between {start} and {end}:{sum_odd}")