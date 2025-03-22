PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age = int(input("Enter your age: "))

    if user_age >=  PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

    if user_age >=  STANLAU_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {STANLAU_AGE}.")
    
    if user_age >=  MAYENGUA_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {MAYENGUA_AGE}.")

if __name__ == '__main__':
    main()