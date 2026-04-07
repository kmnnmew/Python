import sys
input = sys.stdin.readline
from collections import deque

num = int(input()) # 최대 숫자 입력
nums = deque() # 목표 저장
nums2 = [] # 목표 확인
incre = 0 # 최대 숫자까지 증가
stack = [] # 증가하는 애가 저장
result = [] # pop된 애가 저장
tf = True

for _ in range(num):
  input_data = int(input().strip())
  nums.append(input_data)
  nums2.append(input_data)

while tf: 
  if not stack: 
    print('+')
    incre+=1
    stack.append(incre)
  if nums[0] != stack[-1]: 
    print('+')
    incre+=1
    stack.append(incre)
  else:
    nums.popleft()
    result.append(stack.pop())
    print('-')
  if nums2 == result:
    tf = False
  if incre > num: 
    tf = False
    print('NO')
