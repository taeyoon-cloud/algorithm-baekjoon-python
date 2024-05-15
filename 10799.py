# 10799번: 쇠막대기
arr = list(input())
stack = [arr[0]]

floor = 0 # 현재 쌓인 쇠막대기의 층 수
cnt = 0 # 잘려진 쇠막대기 조각의 총 개수


for i in range(1, len(arr)):
    check = arr[i]
    if check == '(':
        stack.append(check)
    
    elif check == ')':
        if stack[-1] == '(':
            stack.pop()
            if arr[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1

print(cnt)
        


