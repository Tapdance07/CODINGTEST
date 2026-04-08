import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
N_set = set()
M_set = set()

for i in range(N):
    N_set.add(sys.stdin.readline().rstrip())

for i in range(M):
    M_set.add(sys.stdin.readline().rstrip())

N_set.intersection_update(M_set)
N_list = list(N_set)
N_list.sort()
print(len(N_list))
for i in N_list:
    print(i)

#N에도 있고 M에도 있는 이름을 찾아야 한다.
#중복이 없다면 우선 set을 사용