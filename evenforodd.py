start = int(input("enter the start of range: "))
end = int(input("enter the end of range: "))

print(f"even numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end =" ")
        
        
print(f"\nodd numbers between {start} and {end}: ")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")