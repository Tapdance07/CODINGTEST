import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    items = {}
    MaxCloth = 1

    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print(0)
        continue

    for _ in range(n):
        name, cate = sys.stdin.readline().rstrip().split()
        if cate not in items:
            items[cate] = 1
        else:
            items[cate] += 1

    for count in items.values():
        MaxCloth *= (count + 1)  # 각 카테고리의 아이템 수 + 1 (선택하지 않는 경우 포함)

    print(MaxCloth - 1)  # 아무것도 선택하지 않는 경우 제외