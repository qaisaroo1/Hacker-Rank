password = input("Enter a password: ")

def checkpassword (password):
    if (len(password)<8):
        return "Invalid Password, Must contain at least 8 character"
    
    has_digit = False
    has_letter = False
    has_uppercase = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        
        if char.isalpha():
            has_letter = True
            if char.isupper():
                has_uppercase = True
        
        if (has_digit  and has_letter and has_uppercase ):
            return "Valid Password"
        else:
            return "Invalid Password"
        
check_password = checkpassword(password)
print(check_password)
            
            