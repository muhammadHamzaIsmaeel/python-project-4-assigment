def main():
  print("=" * 49)
  print("\tWelcome to the Addition Program")
  print("=" * 49)
  num1: str = input("Enter The First Number:")
  num1: int = int(num1)
  num2: str = input("Enter The Second Number:")
  num2: int = int(num2)
  total: int = num1 + num2
  print(f"\n \t   The Sum of {num1} and {num2} is {total}:")
  print("=" * 49)

if __name__ == '__main__':
  main()