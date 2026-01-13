#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non‑negative integer.

    Parameters:
        n (int): A non‑negative integer whose factorial will be computed.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
