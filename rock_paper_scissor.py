from random import randint

print("...Rock...")
print('...Paper...')
print('...Scissors...')

player_1_choice = input("Enter your choice: ").lower()
player_2_choice = randint(1,3)

if player_2_choice == 1:
    player_2_choice = "rock"
elif player_2_choice == 2:
    player_2_choice = "paper"
else:
    player_2_choice = "scissors"

print(f"Player 2 played {player_2_choice}")
print("SHOOT!")

if player_1_choice == player_2_choice:
    print("It's a tie")
else:
    if player_1_choice == "rock":
        if player_2_choice == "paper":
            print("Player 2 wins!")
        elif player_2_choice == "scissors":
            print("Player 1 wins")
    elif player_1_choice == "paper":
        if player_2_choice == "rock":
            print("player 1 wins")
        elif player_2_choice == "scissors":
            print("player 2 wins")
    elif player_1_choice == "scissors":
        if player_2_choice == "rock":
            print("player 2 wins")
        elif player_2_choice == "paper":
            print("Player 1 wins")
        


# if player_1_choice == "Rock" or player_1_choice == "rock":
#     if player_2_choice == "Rock" or player_2_choice == "rock":
#         print("Nobody wins!")
#     elif player_2_choice == "Paper" or player_2_choice == "paper":
#         print("Player 2 wins!")
#     else:
#         print("Player 1 wins!")
# elif player_1_choice == "Paper" or player_1_choice == "paper":
#     if player_2_choice == "Rock" or player_2_choice == "rock":
#         print("Player 1 wins!")
#     elif player_2_choice == "Paper" or player_2_choice == "paper":
#         print("Nobody wins!")
#     else:
#         print("Player 2 wins!")
# else:
#     if player_2_choice == "Rock" or player_2_choice == "rock":
#         print("Player 2 wins!")
#     elif player_2_choice == "Paper" or player_2_choice == "paper":
#         print("Player 1 wins!")
#     else:
#         print("Nobody wins!")