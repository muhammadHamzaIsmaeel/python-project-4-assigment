def main():
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    lst_lenght = len(fruit_lst)
    print(lst_lenght)

    fruit_lst.append('kiwi')

    for fruit in fruit_lst:
        print(fruit)
        
if __name__ == "__main__":
    main()