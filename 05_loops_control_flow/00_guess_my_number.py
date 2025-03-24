import random

def main():

    secrat_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    guess = int(input("Enter a guess: "))

    while guess != secrat_number:
        if guess < secrat_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Enter a new guess: "))

    print(f"Congrats! The number was: {secrat_number}")

if __name__ == '__main__':
    main()
    