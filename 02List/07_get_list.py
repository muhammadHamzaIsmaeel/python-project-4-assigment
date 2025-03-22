def main():
    lst =[]

    val = input("Enter the value: ")
    while val:
        lst.append(val)
        val = input("Enter the value: ")

    print(f"Here's the list: {lst}")    


if __name__ == '__main__':
    main()    