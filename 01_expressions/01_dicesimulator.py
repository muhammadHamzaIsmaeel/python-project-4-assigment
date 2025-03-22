import random

num_in_dice = 6

def roll_dice():
  roll1: int = random.randint(1, num_in_dice)
  roll2: int = random.randint(1, num_in_dice)
  total: int = roll1 + roll2

  print(f"Dice 1: {roll1}")
  print(f"Dice 2: {roll2}")
  print(f"Total of two dice: {total}")
  print("=" *20 + "\n")

def main():
  roll_dice()
  roll_dice()
  roll_dice()
  roll_dice()

if __name__ == '__main__':
  main()