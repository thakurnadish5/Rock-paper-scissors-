from game import play_round

print("=== Rock Paper Scissors ===")

while True:
    print("\nChoose: rock, paper, scissors")
    print("Type 'quit' to exit")

    player_input = input("Your choice: ").lower()

    if player_input == "quit":
        print("Thanks for playing!")
        break

    player, computer, result = play_round(player_input)

    if result == "Invalid choice":
        print("Invalid input! Try again.")
        continue

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    print(f"Result: {result}")
