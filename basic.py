# Factorial (Recursion)
# Computes n! = n × (n–1) × … × 1


def factorial(n):
    # Base case: 0! is 1
    if n == 0:
        return 1
    # Recursive step: n! = n * (n-1)!
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120




# Fibonacci Sequence (Iterative)
# Generates the first n Fibonacci numbers: 0, 1, 1, 2, 3, …


def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        # Shift: new a = old b; new b = old a + old b
        a, b = b, a + b
    return sequence

print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]



# Prime Checker
# Tests whether a number is prime in O(√n) time.


def is_prime(num):
    if num < 2:
        return False
    # Only check divisors up to √num
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

print(is_prime(17))  # Output: True
print(is_prime(18))  # Output: False


# String Palindrome
# Checks if a word reads the same backward and forward.


def is_palindrome(s):
    # Normalize case and compare to its reverse
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Level"))  # Output: True
print(is_palindrome("Hello"))  # Output: False


# Sum of Digits
# Adds each digit in an integer.


def sum_of_digits(n):
    total = 0
    # Extract digits one by one
    while n > 0:
        total += n % 10  # add last digit
        n //= 10         # remove last digit
    return total

print(sum_of_digits(1234))  # Output: 10


# Reverse a List
# Flips the order of elements in a list.


def reverse_list(lst):
    return lst[::-1]  # Python slice that reverses

print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]


# Linear Search
# Finds the index of a target in a list (or –1 if not found).

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

print(linear_search([5, 3, 7, 1], 7))  # Output: 2
print(linear_search([5, 3, 7, 1], 9))  # Output: -1



# Binary Search
# Fast search in a sorted list (O(log n)).


def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3
print(binary_search([1, 3, 5, 7, 9], 2))  # Output: -1


# Bubble Sort
# Simple sorting by repeated swapping (O(n²)).


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # After each pass, the largest element bubbles to the end
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap if out of order
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# Output: [11, 12, 22, 25, 34, 64, 90]



# Greatest Common Divisor (GCD) – Euclid’s Algorithm
# Finds the GCD of two numbers efficiently.


def gcd(a, b):
    # Repeat until remainder is zero
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # Output: 6