num = int(input("Enter a number: "))  # change this value for a different result

# prime numbers are greater than 1
if num > 1:
   # check for factors
   i = 2
   while i * i <= num:
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
       i += 1
   else:
       print(num, "is a prime number")
       
# if input number is less than or equal to 1, it is not prime
else:
   print(num, "is not a prime number")

