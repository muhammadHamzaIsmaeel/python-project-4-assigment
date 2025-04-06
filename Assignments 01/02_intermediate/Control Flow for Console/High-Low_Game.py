import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    your_score = 0

    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1} of {NUM_ROUNDS}")
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        print(f"Your number is: {your_number}")

        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ").lower()

        higher = choice == "higher" and your_number > computer_number
        lower = choice == "lower" and your_number < computer_number

        if higher or lower:
            print("You were right! The computer's number was", computer_number)
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_number)

        print("Your score is:", your_score)
        print('--------------------------------')

    print("\nYour final score is:", your_score)
    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Great job! You did well!")
    else:
        print("Better luck next time!")                        

if __name__ == "__main__":
    main()