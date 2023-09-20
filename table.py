while True:
    
    while True:
        num=eval(input("Enter number for which table to be displayed."))
        till=eval(input("Enter number till multiplication to be performed"))
        if isinstance(num,int)==True and isinstance(till,int)==True and num>=0 and till>=0:
            break
        else:
            print("Please display valid operands")
    
    for i in range(till):
        print(f"{num}x{i+1}={num*(i+1)}")
    
    while True:
        ch=eval(input("Do you wish to perform again? (yes/no)"))
        if ch=="yes" or ch=="no":
            break
        else:
            print("Please display valid choice")
