import sys

# 재귀 깊이 제한 해제 (N이 최대 1,000이므로 넉넉하게 설정)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

# N: 정점의 개수, M: 간선의 개수
n, m = map(int, input().split())

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

# 1번 정점부터 N번 정점까지 확인
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1  # DFS가 새로 시작될 때마다 연결 요소 1개 추가

print(count)