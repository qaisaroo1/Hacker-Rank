num = int(input("Enter a number: "))
orignal_num = num
reverse_num = 0

while (num>0):
    digit = num % 10
    reverse_num = (reverse_num * 10) + digit
    num = num // 10

if (orignal_num == reverse_num):
    print("Number is pallindrome")
else:
    print("Number is not pallindrome")

#Checking String is Pallidrome or not
text = input("Enter a string: ")
reverse_text = text[::-1]

if (text == reverse_text):
    print("String is pallindrome")
else:
    print("String is not a pallidrome")
            
        
    
    
    
    
        
        