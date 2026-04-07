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