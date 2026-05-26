import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "Draw"

    if (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "You Win!"

    return "Computer Wins!"

def play_round(player_choice):
    player_choice = player_choice.lower()

    if player_choice not in choices:
        return None, None, "Invalid choice"

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    return player_choice, computer_choice, result
