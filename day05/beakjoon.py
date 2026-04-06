# # nums = []
# # for i in range(10):
# #   nums.append(int(input()))

# # nums_remain = []

# # for i in range(10): 
# #   nums_remain.append(int(nums[i]%42))

# # print(len(set(nums_remain)))

# num1, num2 = map(int, input().split())

# for i in range(num1, num2+1): 
#   if i < 2: 
#     continue
#   tf = True
#   for num in range(2, int(i**0.5)+1): 
#     if i % num == 0: 
#       tf = False
#       break
#   if tf: print(i)

num = int(input())
data = []
for i in range(num): 
  data.append(input())
for i in range(num): 
  count = 0
  for ch in data[i]: 
    if ch == '(':
      count += 1
    elif ch == ')':
      count -= 1
    if count < 0: 
      break
  print('YES' if count == 0 else 'NO')