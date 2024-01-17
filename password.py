while True :
    password = input("Enter the Password: ")
    
    if len(password) < 12:
        print("Password should be at least 12 characters long")
    else:
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_space = False
        has_special = False  
        
        for char in password:
            if char.isalpha():
                if char.isupper():
                    has_uppercase = True
                elif char.islower():
                    has_lowercase = True
            elif char.isdigit():
                has_digit = True
            elif char.isspace():
                has_space = True
            else:
                has_special = True  
                
        if has_uppercase and has_lowercase and has_digit and not has_space and has_special:
            print("This is a strong Password")
        else:
            print("This is not a strong password plzz try again")
    