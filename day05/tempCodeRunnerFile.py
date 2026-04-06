num = int(input())
result = []

for i in range(num): 
  answer = input()
  if answer[0:4] == 'push':
    result.append(int(answer[5:]))
  elif answer[0:3] == 'pop': 
    if len(result) == 0:
      print(-1)
    else: print(result.pop())
  elif answer[0:3] == 'top': 
    if len(result) == 0:
      print(-1)
    else: print(result[0])
  elif answer[0:4] == 'size': 
    print(len(result))
  elif answer[0:5] == 'empty': 
    print(1 if len(result)==0 else 0)