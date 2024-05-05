# 사용자가 'hello'를 입력하고 엔터를 치는 상황 가정
input1 = input()  # 'hello\n'
input2 = input().rstrip()  # 'hello'

print(input1 == "hello")  # False
print(input2 == "hello")  # True
