def display_available_items(dct):
	# write logic here to display the item in tabular format given below 
    
    
    
    print("      Available Items:")
    print("S.No.     \t    Item     \t      Quanity   \t     Cost/Item  \t     ")
    for s_no, details in dct.items():
        print(f"{s_no:<15} {details['Item']:<50} {details['Quantity']:<55} {details['Cost/Item']:<15}")
    

availableItems ={1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
                2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
                3: {'Item': 'Coffee',   'Quantity': 25,     'Cost/Item': 55},
                4: {'Item': 'Chips', 'Quantity': 10,      'Cost/Item': 50},
                5: {'Item': 'Cream', 'Quantity': 5,        'Cost/Item': 30}}

display_available_items(availableItems)

# display_available_items(availableItems)
# '''
# 		Available Items:
# S.No.          Item           Quanity        Cost/Item      
# 1              Biscuits       5              20.5           
# 2              Chocolates     10             35             
# 3              Coffee         25             55             
# 4              Chips          10             50             
# 5              Cream          5              30 
# '''