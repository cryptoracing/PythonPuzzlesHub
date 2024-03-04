def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two terms

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]

def main() -> object:
    n = int(input("Number of Terms: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci Sequence:", fibonacci_sequence)

main()
