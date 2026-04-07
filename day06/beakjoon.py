# # # # 1427
# # # # num = input();
# # # # nums = ""
# # # # for i in range(len(num)): 
# # # #   nums += sorted(num, reverse=True)[i]
# # # # print(nums)

# # # # 11650
# # # num = int(input())

# # # coor = []

# # # for _ in range(num): 
# # #   coor.append(list(map(int, input().split())))

# # # coor = sorted(coor, key=lambda k : (k[0], k[1]))

# # # for i in coor: 
# # #   print(*i)

# # # 2581
# # num1 = int(input())
# # num2 = int(input())
# # count = []
# # total = 0

# # for i in range(num1, num2+1):
# #   if i < 2: 
# #     continue
# #   tf = True
# #   for num in range(2, int(i**0.5)+1): 
# #     if i%num == 0: 
# #       tf = False
# #       break
# #   if tf: count.append(i)

# # if len(count) > 0: 
# #   for i in count: 
# #     total += i
# #   print(total)
# #   print(min(count))
# # else: print(-1)

# # 10845
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# queue = deque()

# for i in range(n):
#   answer = input().strip()
#   if answer.startswith('push'): 
#     queue.append(int(answer[5:]))
#   elif answer.startswith('pop'):
#     if len(queue) > 0: 
#       print(queue.popleft())
#     else: print(-1)
#   elif answer.startswith('size'):
#     print(len(queue))
#   elif answer.startswith('empty'):
#     if len(queue) > 0: print(0)
#     else: print(1)
#   elif answer.startswith('front'):
#     if len(queue) > 0: 
#       print(queue[0])
#     else: print(-1)
#   elif answer.startswith('back'):
#     if len(queue) > 0: 
#       print(queue[-1])
#     else: print(-1)

# 1874
import sys
from collections import deque
input = sys.stdin.readline

num = int(input()) # 최대 숫자 입력
nums = deque() # 목표 저장
nums2 = [] # 목표 확인
incre = 0 # 최대 숫자까지 증가
stack = [] # 증가하는 애가 저장
result = [] # pop된 애가 저장
result2 = [] # + -가 저장
tf = True

for _ in range(num):
  input_data = int(input().strip())
  nums.append(input_data)
  nums2.append(input_data)

while tf: 
  if not stack: 
    result2.append('+')
    incre+=1
    stack.append(incre)
  if nums[0] != stack[-1]: 
    result2.append('+')
    incre+=1
    stack.append(incre)
  else:
    nums.popleft()
    result.append(stack.pop())
    result2.append('-')
  if nums2 == result:
    tf = False
    for i in result2:
      print(i)
  if incre > num: 
    tf = False
    print('NO')