MINIMUM_HEIGHT : int = 50

def main():
    while True:
        height_user = input("How tall are you? ")

        if height_user == "":
            print("Exiting program. Goodbye!")
            break

        height = float(height_user)

        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
