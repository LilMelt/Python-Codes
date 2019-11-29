import random


def opponent():
    choice = random.choice(["rock", "paper", "scissors"])
    print("Your opponent chose " + choice)
    return choice


def main():
    game = True
    score = 0
    opponent_score = 0
    while game:
        # input user move
        user_move = input("Type \"rock\", \"paper\" or \"scissors\" then press enter: ")
        # check attack is valid
        while user_move != 'rock' and user_move != 'paper' and user_move != 'scissors':
            print("Please enter a valid move")
            user_move = input("Type \"rock\", \"paper\" or \"scissors\" then press enter: ")

        opponent_move = opponent()

        if user_move == 'rock' and opponent_move == 'scissors':
            score += 1
            print("You won! Nice job!")

        elif user_move == 'paper' and opponent_move == 'rock':
            score += 1
            print("You won! Nice job!")

        elif user_move == 'scissors' and opponent_move == 'paper':
            score += 1
            print("You won! Nice job!")

        elif user_move == opponent_move:
            print("You tied!")
        else:
            opponent_score += 1
            print("You lose!")

        # ask user if they want to play again
        play = input("The score is [" + str(score) + "," + str(opponent_score) + "]. Do you want to play another "
                                                                                 "game? Type \"yes\" or \"no\": ")
        # ensure this is a valid input
        while play != 'yes' and play != 'no':
            print("Please enter a valid answer")
            play = input("Do you want to play another game? Type \"yes\" or \"no\": ")

        if play == 'no':
            print("Ok, lets play again soon!")
            game = False
        else:
            print("Ok, lets play another game!")


if __name__ == "__main__":
    main()
