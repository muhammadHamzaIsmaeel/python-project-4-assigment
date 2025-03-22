def main():
  degrees_Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  degrees_celsius = (degrees_Fahrenheit - 32) * 5.0 / 9.0

  print(f"Temperature: {degrees_Fahrenheit}F = {round(degrees_celsius, 2)}C")


if __name__ == '__main__':
  main()