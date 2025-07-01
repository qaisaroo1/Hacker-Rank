import random as rd

list = ["Rock", "Paper", "Scissor"]
Player1_Choice = input("Enter Player 1 your choice: ")
player2_Choice = rd.choice(list)
print("Player2 choice is: " ,player2_Choice)

if (player2_Choice == Player1_Choice):
    print("The game is tie")

elif (player2_Choice == "Rock" and Player1_Choice == "Scissor") or (player2_Choice == "Paper" and Player1_Choice == "Rock") or(player2_Choice == "Scissor" and Player1_Choice == "Paper"):
    print("Player2 wins")

elif (Player1_Choice == "Rock" and player2_Choice == "Scissor") or (Player1_Choice == "Paper" and player2_Choice == "Rock") or (Player1_Choice == "Scissor" and player2_Choice == "Paper"):
    print("Player1 wins")
    
else:
    print("Invlaid inputs")