# 2468번: 안전 영역
import sys
sys.setrecursionlimit(10**9) # 재귀 범위 조절

n = int(input()) # 행, 열 개수

graph = []
max_height= 0 # graph에서 제일 높이가 높은 지역의 높이
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    max_height = max(max(data), max_height)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# dfs
def dfs(x, y, graph, visited, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if not visited[nx][ny] and graph[nx][ny] > h:
                dfs(nx, ny, graph, visited, h)


answer = 1 # 장마철에 물에 잠기지 않는 안전한 영역의 개수
for h in range(max_height):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, graph, visited, h)
                temp += 1
    # print(h, answer, temp)
    answer = max(temp, answer)


print(answer)

