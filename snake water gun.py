import random

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

options = ["snake", "water", "gun"]

print("Welcome to Snake Water Gun Game!")
print("Choices: snake / water / gun")

while True:
    user_choice = input("\nEnter your choice: ").lower()
    if user_choice not in options:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
