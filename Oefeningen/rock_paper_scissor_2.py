from random import randint

game_over = False
wins_player = 0
wins_computer = 0
win_amount = 3

while not game_over:
    print("...Rock...")
    print('...Paper...')
    print('...Scissors...')

    player_1_choice = input("Enter your choice: ").lower()
    player_2_choice = randint(1, 3)

    if player_2_choice == 1:
        player_2_choice = "rock"
    elif player_2_choice == 2:
        player_2_choice = "paper"
    else:
        player_2_choice = "scissors"

    print("SHOOT!")

    if player_1_choice == player_2_choice:
        print("It's a tie")
    else:
        if player_1_choice == "rock":
            if player_2_choice == "paper":
                print("Player 2 wins!")
                wins_computer += 1
            elif player_2_choice == "scissors":
                print("Player 1 wins")
                wins_player += 1
        elif player_1_choice == "paper":
            if player_2_choice == "rock":
                print("player 1 wins")
                wins_player += 1
            elif player_2_choice == "scissors":
                print("player 2 wins")
                wins_computer += 1
        elif player_1_choice == "scissors":
            if player_2_choice == "rock":
                print("player 2 wins")
                wins_computer += 1
            elif player_2_choice == "paper":
                print("Player 1 wins")
                wins_player += 1

    if wins_player == win_amount:
        print("\nPlayer wins the game!!!")
        game_over = True
    elif wins_computer == win_amount:
        print("\nComputer wins the game!!!")
        game_over = True
