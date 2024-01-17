def display_available_items(dict):
    print("\t\tAvailable Items:  ")
    print(f"{'S.No.':<15}{'Item':<15}{'Quanity':<15}{'Cost/Item':<15}")
    for i,j in dict.items():
        print(f"{i:<15}{j['Item']:<15}{j['Quantity']:<15}{j['Cost/Item']:<15}")
    


availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}
display_available_items(availableItems)
CustomerName = input("Enter Customer Name ")
CustomerAddress = input("Enter Customer Address City/State ")
userdemand={}
no_items=eval(input("Enter Number of Items"))
for i in range(no_items):
    item=input("Enter Item Purchased  ")
    quantity=eval(input("Enter Quantity  "))
    userdemand[item]=quantity
print(userdemand)
usercart={}
print("\t\t Items Purchased:  ")
print(f"{'Item':<15}{'Quantity':<15}{'Total Cost':<15}")
for i in userdemand:
    for m,n in availableItems.items():
        if(i!= n['Item'] and userdemand[i]!=n['Quantity']):
            break
        else :
            print("Item not Exist or Quantity is not available  ")

    print(f"{i:<15}{userdemand[i]:<15}{userdemand[i]*0:<15}")