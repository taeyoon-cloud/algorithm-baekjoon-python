# 1931번: 회의실 배정

n = int(input())
arr = [] # 회의 시간을 저장하는 리스트
for _ in range(n):
    time = list(map(int, input().split()))
    arr.append(time)


# 회의 끝 시간 기준으로 오름차순 정렬 / 회의 시작시간 기준으로 오름차순 정렬
arr.sort(key = lambda x:(x[1], x[0])) 


cnt = 1 # 일단 처음 회의는 넣고 시작하므로
end_time = arr[0][1] # 맨 처음 회의의 끝 시간 초기화

for i in range(1, n):
    if arr[i][0] >= end_time: # 확인하는 회의의 시작 시간이 이전 회의의 끝 시간보다 큰 경우
        cnt += 1 # 회의 추가
        end_time = arr[i][1] # 끝 시간은 추가된 회의의 끝 시간으로 변경


print(cnt)