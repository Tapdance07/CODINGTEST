area = [0] * 101


A,B,C = map(int,input().split())
price = [0, A, B*2, C*3]

for _ in range(3):
    start,end = map(int,input().split())
    for i in range(end - start):
        area[start-1+i] += 1
total = 0
for i in range(len(price)):
    total += price[i] * area.count(i)

print(total)