# 7569번: 토마토
from collections import deque
import sys
input = sys.stdin.readline


m, n, h = map(int, input().split())

box = [] # box를 저장하는 리스트
tomato = [] # 초기에 익은 토마토의 (x, y, h) 좌표를 저장하는 리스트
un_tomato_cnt = 0 # 초기에 익지 않은 토마토의 개수를 저장하는 변수
 
for k in range(h):
    each_box = [] # 한 층에 해당하는 박스
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(m):
            if data[j] == 1:
                tomato.append((i, j, k))
            elif data[j] == 0:
                un_tomato_cnt += 1
        each_box.append(data)
    box.append(each_box)

dx = [-1, 1, 0, 0] # x좌표 이동
dy = [0, 0, 1, -1] # y좌표 이동
dh = [-1, 1] # 다른 층으로 이동


# 큐
q = deque([tomato])

day = 0 # 토마토가 모두 익을 때까지 걸리는 최소 일수
while q:
    one_day = q.popleft() # 하루에 익은 토마토의 좌표들을 저장하고 있는 리스트 one_day
    one_day_tomato = [] # (하루에 추가될 익은 토마토의 x좌표, y좌표, 층수)를 저장하는 큐
    for one in one_day:
        x, y, floor = one # 현재 토마토의 x좌표, y좌표, 층수
        
        # 같은 층 토마토 익게 만들기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                # 이미 익은 토마토라면 지나가기.
                if box[floor][nx][ny] == 1 or box[floor][nx][ny] == -1:
                    continue

                box[floor][nx][ny] = 1
                one_day_tomato.append((nx, ny, floor))
                un_tomato_cnt -= 1
        
        # 다른 층 토마토 익게 만들기
        for j in range(2):
            nh = floor + dh[j]

            if nh >= 0 and nh < h:
                if box[nh][x][y] == 1 or box[nh][x][y] == -1:
                    continue
                box[nh][x][y] = 1
                one_day_tomato.append((x, y, nh))
                un_tomato_cnt -= 1


        # 모든 토마토가 익었는지 확인 -> 모든 토마토가 익었다면 반복문 탈출
        if un_tomato_cnt == 0:
            break
    if len(one_day_tomato) > 0: # 만약 하루에 익게 만든 토마토가 있을 때만 큐에 하루에 익은 토마토를 저장하는 리스트 추가
        q.append(one_day_tomato)
    # 하루 경과
    day += 1


# 반복문을 탈출했는데 모든 토마토가 익었다면 day 출력
if un_tomato_cnt == 0:
    print(day - 1)
# 모든 토마토가 익지 않았다면 -1 출력
else:
    print(-1)
