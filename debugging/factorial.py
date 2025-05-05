#!/usr/bin/python3
"""factorial_iterative.py - Calcule la factorielle d'un entier non négatif passé en argument."""

import sys

def factorial(n):
    """
    Calcule la factorielle de n de façon itérative.

    Args:
        n (int): un entier non négatif

    Returns:
        int: la factorielle de n
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémente n à chaque itération
    return result

if __name__ == "__main__":
    # Vérifie que l'utilisateur a bien passé un seul argument
    if len(sys.argv) != 2:
        print("Usage: ./script.py <non-negative integer>")
        sys.exit(1)

    try:
        # Convertit l'argument en entier
        n = int(sys.argv[1])

        # Vérifie que l'entier est non négatif
        if n < 0:
            print("Please enter a non-negative integer.")
            sys.exit(1)

        # Calcule et affiche la factorielle
        f = factorial(n)
        print(f)

    except ValueError:
        # L'argument n'est pas un entier valide
        print("Please enter a valid integer.")
        sys.exit(1)

