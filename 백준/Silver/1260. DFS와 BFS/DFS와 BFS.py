from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, N + 1):
    graph[i].sort()


def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 실행 결과 출력
visited_dfs = [False] * (N + 1)
dfs(V, visited_dfs)
print() # 줄바꿈
bfs(V)