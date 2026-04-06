num1, num2 = map(int, input().split())

for i in range(num1, num2+1): 
  tf = True
  for num in range(2, int(i**0.5)+1): 
    if i % num == 0: 
      tf = False
      break
  if tf: print(i)