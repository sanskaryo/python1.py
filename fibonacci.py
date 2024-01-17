## Program to display the Fibonacci sequence up to n-th term
#
#nterms = int(input("How many terms? "))
#
## first two terms
#n1, n2 = 0, 1
#count = 0
#
## check if the number of terms is valid
#if nterms <= 0:
#   print("Please enter a posit 



def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Call the function
fibonacci(10)
    
