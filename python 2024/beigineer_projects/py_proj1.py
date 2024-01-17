inventory = {}

def add_item(name, price, quantity, category):
    if name not in inventory:
        inventory[name] = {'price': price, 'quantity': quantity, 'category': category}
        print(f"{name} added to the inventory.")
    else:
        print(f"{name} already exists in the inventory. Use 'Update Items' to modify.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item, details in inventory.items():
            print(f"Name: {item}, Price: ${details['price']}, Quantity: {details['quantity']}, Category: {details['category']}")

def update_item(name, price=None, quantity=None, category=None):
    if name in inventory:
        if price is not None:
            inventory[name]['price'] = price
        if quantity is not None:
            inventory[name]['quantity'] = quantity
        if category is not None:
            inventory[name]['category'] = category
        print(f"{name} updated successfully.")
    else:
        print(f"{name} does not exist in the inventory. Use 'Add Items' to add.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} removed from the inventory.")
    else:
        print(f"{name} does not exist in the inventory.")

def search_item(keyword):
    result = [(item, details) for item, details in inventory.items() if keyword.lower() in item.lower() or keyword.lower() in details['category'].lower()]
    if not result:
        print(f"No items found with the keyword '{keyword}'.")
    else:
        print("Search Results:")
        for item, details in result:
            print(f"Name: {item}, Price: ${details['price']}, Quantity: {details['quantity']}, Category: {details['category']}")

def generate_report():
    total_items = len(inventory)
    total_value = sum(details['price'] * details['quantity'] for details in inventory.values())
    low_stock_items = [item for item, details in inventory.items() if details['quantity'] < 5]

    print(f"Inventory Report:")
    print(f"Total Items: {total_items}")
    print(f"Total Stock Value: ${total_value}")
    print(f"Low Stock Items: {', '.join(low_stock_items) if low_stock_items else 'None'}")


# Sample usage
add_item("Laptop", 1000, 10, "Electronics")
add_item("Chair", 50, 20, "Furniture")
add_item("Notebook", 5, 50, "Stationery")

view_inventory()

update_item("Laptop", price=1200, quantity=8)
view_inventory()

remove_item("Chair")
view_inventory()

search_item("note")
search_item("electronic")

generate_report()
