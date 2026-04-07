# 1427
# num = input();
# nums = ""
# for i in range(len(num)): 
#   nums += sorted(num, reverse=True)[i]
# print(nums)

# 11650
num = int(input())

coor = []

for _ in range(num): 
  coor.append(list(map(int, input().split())))

coor = sorted(coor, key=lambda k : (k[0], k[1]))

for i in coor: 
  print(*i)