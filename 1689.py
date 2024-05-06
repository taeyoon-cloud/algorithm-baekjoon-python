# 1689번: 겹치는 선분
import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 선분 개수
arr = [] # (좌표, 시작점,끝점 여부)를 저장하는 리스트
for _ in range(n):
    a,b = map(int,input().rstrip().split())
    arr.append((a,1)) # 선분 시작점에서 +1
    arr.append((b,-1)) # 선분 끝점에서 -1

# 시작점 기준으로 오름차순 정렬
arr.sort()

max_cnt = 0
current_cnt = 0


# 매 점을 확인하면서, 최댓값을 갱신해준다.
for _ , point in arr:
    current_cnt += point
    max_cnt = max(max_cnt,current_cnt)

print(max_cnt)
