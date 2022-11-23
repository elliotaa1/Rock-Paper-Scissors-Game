from random import randint

rockpaperscissors = ["Rock", "Paper", "Scissors"]

randomChoice = rockpaperscissors[randint(0,2)]
print(*randomChoice)

print("Welcome to Rock Paper Scissors!")
print("The computer will choose randomly between rock, paper and scissors and it is your job to win!")
print("First one to 3 points, wins the match.")
playerName = input('First order of business. What is your name? ')

player = 'y'
n = player.lower()
playerCounter = 0
computerCounter = 0
print("Alright !",playerName, ',', end=' ')
while computerCounter < 3 and playerCounter < 3 or n == 'y':
    player = input("Rock, Paper or Scissors? ")

    if player.lower() == randomChoice.lower():
        print("Tie! No points awarded for both sides!")
    elif player.lower() == 'rock':
        if randomChoice.lower() == 'paper':
            print("You lose !", randomChoice,"covers", player)
            computerCounter +=1
            print("The computer has: "+str(computerCounter)+ " points.")
        else:
            print("You won!", player,'smashes', randomChoice)
            playerCounter +=1
            print("You now have: "+str(playerCounter)+ " points.")
    elif player.lower() == 'scissors':
        if randomChoice.lower() == 'rock':
            print("You lose!", randomChoice,'smashes', player)
            computerCounter +=1
            print("The computer has: "+str(computerCounter)+ " points.")
        else:
            print("You win!", player,'cuts', randomChoice)
            playerCounter +=1
            print("You now have: "+str(playerCounter)+ " points.")
    elif player.lower() == 'paper':
        if randomChoice.lower() == 'scissors':
            print("You lose!", randomChoice, 'cuts', player)
            computerCounter +=1
            print("The computer has: "+str(computerCounter)+ " points.")
        else:
            print('You win!', player,'covers', randomChoice)
            playerCounter +=1
            print("You now have: "+str(playerCounter)+ " points.")
    else:
        print("Invalid input. No point awarded. Try again.")
    

    if computerCounter == 3:
        print("The computer has won.")
        replay = input("Would you like to play again? Y/N: ")
        if replay.lower() == 'y':
            playerCounter = 0
            computerCounter = 0
            print("Game is restarting . . . .")
        if replay.lower() == 'n':
            print("Thanks for playing!")
            break
        while replay.lower() != 'y' and replay.lower() !='n':
            print("Invalid input. Try again")
            replay = input("Would you like to play again? Y/N: ")
   
    if playerCounter == 3:
        print("Congratulations! You won!")

        replay = input("Would you like to play again? Y/N: ")
        if replay.lower() == 'y':
            playerCounter = 0
            computerCounter = 0
            print("Game is restarting . . . .")
        if replay.lower() == 'n':
            print("Thanks for playing!")
            break
        while replay.lower() != 'y' and replay.lower() !='n':
            print("Invalid input. Try again")
            replay = input("Would you like to play again? Y/N: ")
   

    randomChoice = rockpaperscissors[randint(0,2)]
    print(*randomChoice)
