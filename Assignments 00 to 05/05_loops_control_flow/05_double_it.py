greater_than =  int(100)

def main():
    user = int(input("Enter the number: "))

    while user < greater_than:
        user = user * 2
        print(user, end=" ")

if __name__ == '__main__':
    main()
