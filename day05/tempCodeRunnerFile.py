num = int(input())
data = []
for i in range(num): 
  data.append(input())
for j in range(num): 
  data2 = {}
  for i in data[j]:
    data2[i] = data2.get(i, 0)+1
  if data2.get('(', 0) == data2.get(')', 0): 
    print('YES')
  else: print('NO')