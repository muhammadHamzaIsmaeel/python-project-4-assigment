def double(num: int):
    return num * 2

def main():
    num = int(input("Enter The Number: "))
    num_double = double(num)
    print(f"Double that is {num_double}")

if __name__ == '__main__':
    main()    