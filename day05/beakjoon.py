nums = []
for i in range(10):
  nums.append(int(input()))

nums_remain = []

for i in range(10): 
  nums_remain.append(int(nums[i]%42))

count = {}

for num in nums_remain:
  count[num] = count.get(num, 0)+1

print(len(count))