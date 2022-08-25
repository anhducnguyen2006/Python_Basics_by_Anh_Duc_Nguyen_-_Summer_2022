import random as rd

def rockpaperscissors(ans):
    counter = rd.choice(["rock","paper","scissors"])
    print("Computer: " + counter)
    print("")
    if ans == "paper" and counter == "rock":
        print("You win!")
    elif ans == "paper" and counter == "paper":
        print("Draw!")
    elif ans == "paper" and counter == "scissors":
        print("You lose!")
    elif ans == "rock" and counter == "paper":
        print("You lose!")
    elif ans == "rock" and counter == "rock":
        print("Draw!")
    elif ans == "rock" and counter == "scissors":
        print("You win!")
    elif ans == "scissors" and counter == "rock":
        print("You lose!")
    elif ans == "scissors" and counter == "scissors":
        print("Draw!")
    elif ans == "scissors" and counter == "paper":
        print("You win!")
    else:
        print("That's not an option!")
def main():
    print("Rock Paper Scissors\n")
    ans = input("Your choice: ")
    rockpaperscissors(ans)
    
if __name__ == "__main__":
    main()
