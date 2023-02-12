visited = [False] * 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def dfs(v):
    print(v, end=' ')
    
    for adj in graph[v]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj)

visited[1] = True
dfs(1)
