# 9663번: N-Queen

n = int(input())

visited = [[False] * (n+2) for _ in range(n+2)]
visited_row = [False] * (n+2) # 1~n번 행에 퀸이 놓였는지 안 놓였는지 확인하기 위한 리스트

answer = 0


# 대각선 검사
def is_promising(visited, i, num):
    temp = 1
    for x in range(num-1, 0, -1):
        if  i - temp > 0 and visited[i-temp][x]:
            return False
        if i + temp < n+1 and visited[i+temp][x]:
            return False
        temp += 1
    return True



def backTracking(num):
    global answer
    if num == n + 1:
        answer += 1
        return
    
    is_no_place = True

    for i in range(1, n+1): # 1~n번째 행에 퀸을 놓을 수 있다.
        if not visited_row[i]:
            if is_promising(visited, i, num):
                is_no_place = False
                visited_row[i] = True
                visited[i][num] = True
                backTracking(num + 1)
                visited_row[i] = False
                visited[i][num] = False
    
    if is_no_place:
        return
    



            


backTracking(1)
print(answer)