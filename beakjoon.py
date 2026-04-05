# num = input();
# nums = input().split();

# print(f"{min(map(int, nums))} {max(map(int, nums))}")

nums = {}
for i in range(9): 
  nums[i] = int(input());
print(max(nums.values()))
print(max(nums, key=nums.get)+1)