import random

def main():
    
    secret_number = random.randint(1, 99)
    attempts = 5

    print("\nI am thinking of a number between 1 and 99...")
    print(f"You have {attempts} attempts to guess the number.\n")


    while attempts > 0:
        guess = int(input("Take a guess: "))
        attempts -= 1
        if guess < secret_number:
            print(f"Your guess is too low. {attempts} attempts left.\n")
        elif guess > secret_number:
            print(f"Your guess is too high. {attempts} attempts left.\n")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly! 🎉")
            return 
        
    print(f"Game Over! The secret number was: {secret_number}")    

if __name__ == "__main__":
    main()        

