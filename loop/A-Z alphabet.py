print("A-Z Alphabet Patterns")
# This function prints various patterns of alphabets using asterisks


def print_alphabet_patterns(size=5):
    # Pattern A
    print("\nA Pattern:")
    for i in range(size):
        for j in range(size*2-1):
            if (i == 0 and j == size-1) or \
               (i == size//2 and (j >= size//2 and j <= size+size//2-1)) or \
               (j == size-1-i or j == size-1+i) and i > 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern B
    print("\nB Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or \
               (i == 0 or i == size//2 or i == size-1) and j < size-1 or \
               j == size-1 and (i != 0 and i != size//2 and i != size-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern C
    print("\nC Pattern:")
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size-1) and j > 0 or \
               j == 0 and (i != 0 and i != size-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern D (already shown)
    print("\nD Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or \
               (i == 0 or i == size-1) and j < size-1 or \
               j == size-1 and (i != 0 and i != size-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern E
    print("\nE Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or \
               i == 0 or i == size//2 or i == size-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern F
    print("\nF Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or \
               i == 0 or i == size//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern G
    print("\nG Pattern:")
    for i in range(size):
        for j in range(size):
            if (i == 0 or i == size-1) and j > 0 or \
               j == 0 and (i != 0 and i != size-1) or \
               (j == size-1 and i >= size//2) or \
               (i == size//2 and j >= size//2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern H (already shown)
    print("\nH Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size-1 or i == size//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern I
    print("\nI Pattern:")
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == size//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern J (already shown)
    print("\nJ Pattern:")
    for i in range(size):
        for j in range(size):
            if i == 0 or \
               (j == size//2 and i < size-1) or \
               (i == size-1 and j < size//2) or \
               (j == 0 and i > size-2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern K (already shown)
    print("\nK Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or \
               i + j == size-1 or \
               i == j and i > size//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern L (already shown)
    print("\nL Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or i == size-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern M (already shown)
    print("\nM Pattern:")
    width = size + 2
    for i in range(size):
        for j in range(width):
            if j == 0 or j == width-1 or \
               (i == j and i <= width//2) or \
               (i + j == width-1 and i <= width//2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern N (already shown)
    print("\nN Pattern:")
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size-1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Pattern O
    print("\nO Pattern:")
    for i in range(size):
        for j in range(size):
            if ((i == 0 or i == size-1) and (j > 0 and j < size-1)) or \
               ((j == 0 or j == size-1) and (i != 0 and i != size-1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Continue with P-Z patterns following the same structure...

print_alphabet_patterns(5)