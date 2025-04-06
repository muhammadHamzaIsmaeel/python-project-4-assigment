def average(a: float, b: float):
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(3, 10)
    avg_2 = average(8, 10)

    final = average(avg_1, avg_2)
    print(f"avg 1: {avg_1}")
    print(f"avg 2: {avg_2}")
    print(f"Total: {final}")

if __name__ == '__main__':
    main()