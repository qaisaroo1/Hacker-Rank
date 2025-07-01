import random as rd

rand = rd.randint(1,100)
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))

    if (user_guess == rand):
        print("Guess correctly")
        break
    
    elif (user_guess > rand):
        print("too High")
    
    elif (user_guess < rand):
        print("too Low")
