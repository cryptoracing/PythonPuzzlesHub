def generate_fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = generate_fibonacci_recursive(n - 1)
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence

def main():
    n = int(input("Number of Terms: "))
    fibonacci_sequence = generate_fibonacci_recursive(n)
    print("Fibonacci Sequence:", fibonacci_sequence)

main()
