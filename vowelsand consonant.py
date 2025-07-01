name = "HelloWorld"
vowelCount = 0
consonantCount = 0
for i in range(0,10):
    if (name[i] == 'a' or name[i] == 'e'or name[i] == 'i' or name[i] == 'o' or name[i] == 'u'):
        vowelCount += 1
    
    else : 
        consonantCount += 1
        
print("Number of vowel: " ,vowelCount)
print("number of consonant: " ,consonantCount)
