userDemand = {}
customerName = input("Enter Customer Name: ")
customerAddress = input("Enter Customer Address (City/State): ")
numberOfItem = int(input('Enter the number of items to be purchased: '))

for _ in range(numberOfItem):
    item = input('Enter the Item Name: ') 
    quantity = int(input('Enter the Quantity: '))
    userDemand[item] = quantity

print(f"Customer Name: {customerName} \nCustomer Address: {customerAddress} \nItems to be purchased: {userDemand}")
