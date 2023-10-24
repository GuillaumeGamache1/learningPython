import random



def chooseRPS():

    

    while True:
     choice = input("Rock, Paper or Scissors (please type it): ").upper()
     if choice not in ('ROCK', 'PAPER', 'SCISSORS'):
            print("Wrong input, enter either Rock, Paper or Scissors")
     else:
        return choice

def computerChoice():

    
    

    randomNum = random.randint(1, 3)

    if randomNum == 1:
        pcChoice = 'Rock'.upper()
    elif randomNum == 2:
        pcChoice = 'Paper'.upper()
    else:
        pcChoice = 'Scissors'.upper()
    
    return pcChoice

def compare(playerChoice, pcChoice):
    
    

    if playerChoice == pcChoice:
        return "Tie"
    elif (playerChoice == "ROCK" and pcChoice == "SCISSORS") or \
         (playerChoice == "SCISSORS" and pcChoice == "PAPER") or \
         (playerChoice == "PAPER" and pcChoice == "ROCK"):
         return "Win"
    else:
        return "Lose"

def printResult(playerchoice, pcchoice, result):
    print("You chose " + playerchoice + " and the pc chose " + pcchoice + " so it's a " + result)

def addPoint(result, x, y):
    if result == "Win":
        x += 1
        
    elif result == "Lose":
        y += 1
    
    return x, y
    
def scores(x, y):
    print("Player has " + str(x) + " points, and the PC has " + str(y) + " points.")

def playAgain(x):
    while True:
        ans = input("Would you like to play again? (Y/N): ").upper()
        
        if ans == 'Y':
            return x
        elif ans == 'N':
            x = False
            return x
        else:
            print("Please type Y or N")


def main():
  x = True
  playerPts = 0
  pcPts = 0
  while  x is True:  
    pcChoice = computerChoice()
    choice = chooseRPS()
    result = compare(choice, pcChoice)
    printResult(choice, pcChoice, result)
    playerPts, pcPts = addPoint(result, playerPts, pcPts)
    scores(playerPts, pcPts)
    x = playAgain(x)
    





main()
    
    




    



