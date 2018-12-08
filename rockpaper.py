import random
import score

print("This is a rock-paper-scissors simulator")
print("Press 'q' to quit")

while True:
    comp_throw = random.randint(1,3)

    user_throw = input("Rock, Paper, or Scissors? ")


    if user_throw.lower() == "rock":
        print("You choose ROCK!")
    elif user_throw.lower() == "paper":
        print("You choose PAPER!")
    elif user_throw == 'q':
        break
    elif user_throw.lower() == 'scissors':
        print("You choose SCISSORS!")
    else:
        print("Choose one!")
        continue

    print("1....")
    print("2....")
    print("3....")
    print("SHOOT!")

    if comp_throw == 1:
        comp_throw = "rock"
        print("Your opponent chooses ROCK!")
    elif comp_throw == 2:
        comp_throw = "paper"
        print("Your opponent chooses PAPER!")
    elif comp_throw == 3:
        comp_throw = "scissors"
        print("Your opponent chooses SCISSORS!")

    if user_throw == comp_throw:
            print("DRAW!")
    elif user_throw == "rock" and comp_throw == "scissors":
            print("You win!")
            score.add_point("Player")
    elif user_throw == "Rock" and comp_throw == "paper" :
            print("Your opponent wins!")
            score.add_point("comp")
    elif user_throw == "paper" and comp_throw == "rock":
            print("You win!")
            score.add_point("Player")
    elif user_throw == "paper" and comp_throw == "scissors":
            print("Your opponent wins!")
            score.add_point("comp")
    elif user_throw == "scissors" and comp_throw == "rock":
            print("Your opponent wins!")
            score.add_point("comp")
    elif user_throw == "scissors" and comp_throw == "paper":
            print("You win!")
            score.add_point("Player")
