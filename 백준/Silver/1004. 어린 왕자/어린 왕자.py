import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    dis = list(map(int, sys.stdin.readline().split()))
    planet = int(sys.stdin.readline())
    count = 0
    for _ in range(planet):
        plant = list(map(int, sys.stdin.readline().split()))


        d1 = math.sqrt((dis[0] - plant[0]) ** 2 + (dis[1] - plant[1]) ** 2)

        d2 = math.sqrt((dis[2] - plant[0]) ** 2 + (dis[3] - plant[1]) ** 2)


        if (d1 < plant[2]) != (d2 < plant[2]):
            count += 1

    print(count)
