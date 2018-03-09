from random import randint

game_over = False
next_game = 'y'

# Keep playing "till player wants to quit"
while next_game == 'y':
    # Get a new random number between 1 and 10
    random_number = randint(1, 11)

    # Empty variable guess
    guess = None
    # Keep looping 'till guess is the same as the random number
    while guess != random_number:
        # Ask for a guess
        print("Guess between 1 and 10: ")
        guess = int(input())

        # Compare guess and random number
        if guess == random_number:
            print('You win!')
        elif guess < random_number:
            print('Too low!')
        else:
            print("Too high!")

    # Keep asking 'till valid input
    next_game = ''
    while next_game.lower() != "y" and next_game.lower() != "n":
        print("Want to play another game? (y/n)")
        next_game = input()
