import sys

S = int(sys.stdin.readline())

def max_count_of_unique_numbers(S):
    count = 0
    current = 1

    while S >= current:
        S -= current
        count += 1
        current += 1

    return count
print(max_count_of_unique_numbers(S))