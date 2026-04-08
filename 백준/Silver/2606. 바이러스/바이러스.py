import sys

def dfs(networks, v, visited):
    visited[v] = True
    for z in networks[v]:
        if not visited[z]:
            dfs(networks, z, visited)


N = int(sys.stdin.readline().rstrip())
network = int(sys.stdin.readline().rstrip())
networks = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


for i in range(network):
    A,B = map(int,sys.stdin.readline().rstrip().split())
    networks[A].append(B)
    networks[B].append(A)



dfs(networks,1,visited)
print(sum(visited)-1)




