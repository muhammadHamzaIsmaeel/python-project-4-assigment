DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    print(f"There are {DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN} seconds in a year!")

    choice_year:int = int(input("\nEnter years to convert seconds: "))

    print(f"There are {choice_year * DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN} seconds in {choice_year} years!")

if __name__ == '__main__':
    main()