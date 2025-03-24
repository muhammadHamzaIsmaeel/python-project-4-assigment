def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print(f"This fruit is in stock! Here is how many: {stock}")

def num_in_stock(fruit):
    if fruit == 'apple':
        return 4
    if fruit == 'durian':
        return 43
    if fruit == 'pear':
        return 10
    else:
        return 0

if __name__ == '__main__':
    main()            
		   