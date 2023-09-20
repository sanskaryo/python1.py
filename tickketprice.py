age=int(input("please enter the age of the person : "))

if age<3:
    ticket_price = 0
elif age >4 or age<12:
    ticket_price = 10

elif age>13 or age<17 :
    ticket_price = 15
    
else:
    ticket_price = 20
    
print(f"the ticket price is{ticket_price}")
    
