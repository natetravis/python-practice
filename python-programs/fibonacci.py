def fibonacci(n):

    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return only the first number
    elif n == 2:
        return [0, 1]  # Return the first two numbers

    # Start with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the rest of the sequence
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Example Usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
