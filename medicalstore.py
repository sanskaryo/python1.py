#Medical store management system 

while True :
    
    store_database = []
    
    print("===Store Management System===")
    
    print("1. Add medecine")
    
    print("2. Display medecine Inventory:")
    
    print("3. Update Medecine Quantity")
    
    print("4. Seacrch Medecine By id")
    
    print("5. Exit")
    
    choice = (input("enter your choice : "))
    
    if choice == '1':
    
        Id = int(input("enter id "))
        
        Name = input("enter medecine name ")
        
        Quantity = int(input("enter the no of quantity "))
        
        Price = int(input("enter the price "))
        
        store_database.append({'medecine_Id': Id, 'name': Name , 'Quantity' : Quantity , 'price' : Price} )
        
        print(f"medecine  added succesfully")
        
    elif choice == '2' :
        print("display Inventory")
        for medecine in store_database:
            print(f"medecine id : {Id['Id']}\n medecine name : {Name['name']}\n medecine quantity : {Quantity['quantity']} Price : {Price['price']}\n")
        
        
    elif choice == '3':
    
        
    
        print("Update Details Menu:")
        ask = (input("Enter medecine id to update details: "))
        if ask in store_database:
            history = input("Enter Updated Quantity: ")
            details = medecine[ask]
            details[2] = Quantity
            print(f"medecine quantity [{ask}].")
        else:
            print("medecine not found")
        
        
    elif choice == '4':
        print("search medecine on id")
        
        medecine_id = int(input("Enter the medecine ID: "))
        if 0 < medecine_id <= len(store_database):
            medecine = store_database[medecine - 1]
            print(f"medecine Information for ID {medecine_id}:\nname: {Name['Name']}\nQuantity: {Quantity['Quantity']}\nPrice: {Price['Price']}\n")
        else:
            print("Invalid medecine ID.")  
            
    elif choice == '5':
        print("exiting")
        break
        
        
        
        
        
        
        
        
        
   