import random

def roll_dice():
    while True:
        # Simulate rolling a dice
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
        
        # Ask the user if they want to roll again
        roll_again = input("Roll again? (yes/no): ").strip().lower()
        if roll_again != 'yes':
            print("Thanks for playing!")
            break

# Run the dice simulator
if __name__ == "__main__":
    roll_dice()