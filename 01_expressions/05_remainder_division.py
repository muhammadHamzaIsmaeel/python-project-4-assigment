def main():
  dividend: int = int(input("Please enter an integer to be divided: "))
  divisor: int = int(input("Please enter an integer to divide by: "))

  quotient: int = dividend // divisor
  remainder: int = dividend % divisor

  print(f"\nThe result of this division is {quotient}  with a remainder of {remainder}")

if __name__ == '__main__':
  main()