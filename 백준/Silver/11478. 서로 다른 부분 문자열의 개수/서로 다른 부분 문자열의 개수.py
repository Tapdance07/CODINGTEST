import sys

s = (sys.stdin.readline().rstrip())

n = len(s)
substrings = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        substrings.add(s[i:j])

print(len(substrings))