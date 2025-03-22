import math
import random

Num_side = 6

def main():
  dice1: int = random.randint(1, Num_side)
  dice2: int = random.randint(1, Num_side)

  total: int = dice1 + dice2

  print("Dice have", Num_side, "sides each.")
  print("First die:", dice1)
  print("Second die:", dice2)
  print("Total of two dice:", total)

if __name__ == '__main__':
  main()