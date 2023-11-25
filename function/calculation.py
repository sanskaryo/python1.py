# def calcultator(a,b):

    
#     print (a+b)
#     print (a-b)
#     print (a*b)
#     print (a//b)
#     print (a%b)

# a,b = map(int,input().split())

# print (calcultator(a,b))


















def calculator(a, b):
    results = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "integer division": a // b,
        "modulus": a % b
    }
    return results

a, b = map(int, input().split())
results = calculator(a, b)

for operation, result in results.items():
    print(f"The result of {operation} is {result}")
