#!/usr/bin/python3
"""factorial.py - Computes the factorial of a non-negative integer from command-line argument."""

import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer recursively.

    Args:
        n (int): The number for which to compute the factorial.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Ensure exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        # Try to convert argument to integer
        n = int(sys.argv[1])

        # Compute and print the factorial
        result = factorial(n)
        print(result)

    except ValueError:
        # Handle non-integer or negative input
        print("Please enter a valid non-negative integer.")
        sys.exit(1)

