# 1926번: 그림(DFS)
import sys
sys.setrecursionlimit(10**6)

cnt = 0 # 그림의 개수
max_area = 0 # 가장 넓은 그림의 넓이

n, m = map(int, input().split())
visited = [[False]* m for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0 , 0]


def dfs(x, y):
    visited[x][y] = True
    global area
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny < m and ny >= 0:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                area += 1
                dfs(nx, ny)





for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            area = 1
            dfs(i, j)
            cnt += 1
            max_area = max(area, max_area)



print(cnt)
print(max_area)