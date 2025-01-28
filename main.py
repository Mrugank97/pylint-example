import math

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of prime numbers up to a limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def factorial(number):
    """Calculate the factorial of a number."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def main():
    """Main function to demonstrate functionality."""
    print("Welcome to the Python utility program!")

    # Prime number generation
    limit = 50
    print(f"Generating prime numbers up to {limit}:")
    primes = generate_primes(limit)
    print(primes)

    # Factorial calculation
    number = 5
    print(f"Calculating the factorial of {number}:")
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}")

    # Prime check
    test_number = 29
    print(f"Checking if {test_number} is a prime number:")
    result = is_prime(test_number)
    print(f"{test_number} is {'a prime' if result else 'not a prime'} number.")

if __name__ == "__main__":
    main()
