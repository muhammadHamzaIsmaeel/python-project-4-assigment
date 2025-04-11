import random

print("Strong Password Generator")

def main():
  char = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()_+,.1234567890'

  number = int(input("Amount of password to generate: "))
  length = int(input("Enter your password length: "))

  print("\nYour Password")

  for pwd in range(number):
    passwords = ''
    for c in range(length):
      passwords += random.choice(char)
    print(passwords)

if __name__ == '__main__':
  main()