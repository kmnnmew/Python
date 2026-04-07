# 1427
# num = input();
# nums = ""
# for i in range(len(num)): 
#   nums += sorted(num, reverse=True)[i]
# print(nums)

# 11650
# num = int(input())

# coor = []

# for _ in range(num): 
#   coor.append(list(map(int, input().split())))

# coor = sorted(coor, key=lambda k : (k[0], k[1]))

# for i in coor: 
#   print(*i)

# 2581
# num1 = int(input())
# num2 = int(input())
# count = []
# total = 0

# for i in range(num1, num2+1):
#   if i < 2: 
#     continue
#   tf = True
#   for num in range(2, int(i**0.5)+1): 
#     if i%num == 0: 
#       tf = False
#       break
#   if tf: count.append(i)

# if len(count) > 0: 
#   for i in count: 
#     total += i
#   print(total)
#   print(min(count))
# else: print(-1)

