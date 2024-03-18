# 14503번: 로봇 청소기
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 방의 크기
r, c, d = map(int, input().split()) # 로봇 초기 위치, 바라보는 방향(0 ~ 3 -> 북, 동, 남, 서)

graph = [list(map(int, input().split())) for _ in range(n)] # 방 상태 입력

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0 # 로봇 청소기가 작동을 시작한 후, 작동을 멈출 때까지 청소하는 칸의 개수

x = r
y = c
while True:
    if graph[x][y] == 0: # 현재 칸이 청소되지 않은 경우
        graph[x][y] = 2 # 현재 칸을 청소
        answer += 1

    
    temp = 4 # 주변 4칸 중 청소되지 않은 빈 칸의 개수
    for i in range(d-1, d-5, -1):
        i %= 4
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0:
                x = nx
                y = ny
                d = i
                break
        
        temp -= 1

    if temp == 0: # 만약 현재 칸 주변 4칸 중 청소되지 않는 빈 칸이 없는 경우
        nx = x - dx[d] 
        ny = y - dy[d]

        # 바라보는 방향을 유지한 채로 한칸 후진
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] != 1: # 후진 할 수 있다면, 후진하고 다시 반복문
                x = nx
                y = ny

            elif graph[nx][ny] == 1: # 후진 할 수 없다면, 작동을 멈춤
                break
    

print(answer)
    
