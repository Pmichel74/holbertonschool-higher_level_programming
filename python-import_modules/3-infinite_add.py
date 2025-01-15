#!/usr/bin/python3

# prints the result of the addition of all arguments
# Vérifie si le script est exécuté directement
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
