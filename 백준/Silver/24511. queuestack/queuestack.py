import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
DataCon = list(map(int,sys.stdin.readline().rstrip().split()))
Datalist = deque()
Datalist.extend(map(int,sys.stdin.readline().rstrip().split()))
Data_N = int(sys.stdin.readline().rstrip())
input_Data = list(map(int,sys.stdin.readline().rstrip().split()))
# Datalist.extendleft(input_Data)
ans = list()

#선입 선출인 DataCon이 0인 애들만 확인하면 되는데
for i in range(N):
    if Data_N > len(ans):
     if DataCon[-i-1] == 0:
        ans.append(Datalist[-i-1])
    else:
        break

if len(ans)<Data_N:
    for i in range(Data_N-len(ans)):
        ans.append(input_Data[i])

print(*ans)