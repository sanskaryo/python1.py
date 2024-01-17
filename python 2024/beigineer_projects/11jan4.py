def display_user_cart(cart):
    print("User Cart:")
    for item in cart.values():
        print(f"{item['Quantity']} {item['Item']} - ${item['TotalCost']}")

availableItems = {
    1: {'Item': 'Biscuits', 'Quantity': 20, 'Cost/Item': 2},
    2: {'Item': 'Chocolates', 'Quantity': 30, 'Cost/Item': 1.5},
    3: {'Item': 'Coffee', 'Quantity': 50, 'Cost/Item': 5},
    4: {'Item': 'Chips', 'Quantity': 20, 'Cost/Item': 3},
    5: {'Item': 'Cream', 'Quantity': 10, 'Cost/Item': 4}
}

userDemand = {'Biscuits': 5, 'Chocolates': 10, 'Coffee': 25, 'Chips': 10, 'Creami': 5}
name = 'Sanskar'
address = 'Gla university Mathura'
distance = 25
deliveryCharge = 70
bill = 0

user_cart = {key: {'Item': availableItems[key]['Item'], 'Quantity': 0, 'TotalCost': 0} for key in availableItems}
for item in userDemand:
    for key in availableItems:
        if item == availableItems[key]['Item']:
            if userDemand[item] <= availableItems[key]['Quantity']:
                total_cost = userDemand[item] * availableItems[key]['Cost/Item']
                bill += total_cost
                availableItems[key]['Quantity'] -= userDemand[item]
                user_cart[key]['Quantity'] = userDemand[item]
                user_cart[key]['TotalCost'] = total_cost
            else:
                print(f"Sorry, we don't have enough {item} in stock")
                user_cart.pop(key)
                break

totalBill = bill + deliveryCharge
display_user_cart(user_cart)
print('Total Item Cost:', bill)
print('Total Bill Amount = Total Amount + delivery charge:', totalBill)
customer_details = {'Name': name, 'Address': address, 'Distance': distance, 'Delivery Charge': deliveryCharge, 'Bill': totalBill}
print(customer_details)