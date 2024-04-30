def fibonacci_generator(length):
    a, b = 0, 1
    for _ in range(length):
        yield a
        a, b = b, a + b

def main():
    try:
        length = int(input("Enter the length of Fibonacci sequence: "))
        if length <= 0:
            print("Length have to be positive integer.")
            return
        fibonacci_sequence = list(fibonacci_generator(length))
        print("Fibonacci sequence length", length, "is:", fibonacci_sequence)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
