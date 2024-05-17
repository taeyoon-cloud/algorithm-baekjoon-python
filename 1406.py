# 1406번: 에디터

# 1. 큐 활용 풀이
import sys
from collections import deque
input = sys.stdin.readline

# 커서를 기준으로 스택 2개로 분리
left = deque(list(input().rstrip()))
right = deque([])

n = int(input()) # 명령 개수


for _ in range(n):
    command = input().rstrip()

    # 커서를 왼쪽으로 옮김
    # left에서 pop해서 right에 push
    if command == 'L':
        if left:
            char = left.pop()
            right.appendleft(char)
    # 커서를 오른쪽으로 옮김
    # right에서 pop해서 left에 push
    elif command == 'D':
        if right:
            char = right.popleft()
            left.append(char)
    # 커서 왼쪽에 있는 문자 삭제
    # left에서 pop
    elif command == 'B':
        if left:
            left.pop()
    # 커서 왼쪽에 문자 추가
    # left에 push
    else:
        command, char = command.split()
        left.append(char)


print("".join(left + right))




# 2. 스택 활용 풀이
# import sys
# input = sys.stdin.readline

# left = list(input().rstrip())
# right = []

# n = int(input()) # 명령 개수


# for _ in range(n):
#     command = input().rstrip()

#     if command == 'L':
#         if left:
#             char = left.pop()
#             right.append(char)

#     elif command == 'D':
#         if right:
#             char = right.pop()
#             left.append(char)

#     elif command == 'B':
#         if left:
#             left.pop()

#     else:
#         command, char = command.split()
#         left.append(char)


# print("".join(left) + "".join(right[::-1]))