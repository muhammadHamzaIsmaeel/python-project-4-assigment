import random

x = random.randint(10, 100)

def guess():
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_number:
      print("Sorry, guess again. To low.")
    elif guess > random_number:
      print("Sorry, guess again. To high. ")
  print(f"Congrats. You have guess the number {random_number} correctly! ")

guess()