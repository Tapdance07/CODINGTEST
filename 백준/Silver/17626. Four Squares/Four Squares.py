import sys
import math

def min_square_count(n):
    # Case 1: If n is a perfect square, return 1
    if math.isqrt(n) ** 2 == n:
        return 1

    # Case 2: Check if n can be expressed as the sum of two squares
    for i in range(1, int(math.sqrt(n)) + 1):
        if math.isqrt(n - i * i) ** 2 == (n - i * i):
            return 2

    # Case 3: Check if n follows the 4^k * (8m + 7) rule
    temp = n
    while temp % 4 == 0:  # Remove factors of 4
        temp //= 4
    if temp % 8 == 7:  # If remaining part follows (8m + 7) form
        return 4

    # Case 4: If none of the above, return 3
    return 3

# Read input
n = int(sys.stdin.readline().strip())
print(min_square_count(n))
