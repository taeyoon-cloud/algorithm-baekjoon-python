# 10799번: 쇠막대기
import sys
input = sys.stdin.readline

arr = list(input())
stack = [arr[0]]

cnt = 0 # 잘려진 쇠막대기 조각의 총 개수


for i in range(1, len(arr)):
    check = arr[i]
    # 만약 현재 넣으려는 괄호가 '('인 경우에는 stack에 집어 넣는다.
    if check == '(':
        stack.append(check)
    # 만약 현재 넣으려는 괄호가 ')'인 경우에는 더 구체적으로 확인한다.
    elif check == ')':
        stack.pop() # stack에는 항상 '('만 들어간다.
        if arr[i-1] == '(': # 만약 check 바로 전 괄호가 '('라면 현재 쌓인 쇠막대기 층 수만큼 cnt에 더해준다.
            cnt += len(stack)
        else: # 만약 check 바로 전 괄호가 ')'라면 check는 쇠막대기의 끝을 가리키는 것이므로 1만 더해준다.
            cnt += 1

print(cnt)
        


