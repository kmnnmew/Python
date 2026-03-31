def add():
  a = int(input("첫 번째 숫자: "));
  b = int(input("두 번째 숫자: "));
  print(f"결과: {a} + {b} = {a+b}")
  return a+b

def sub():
  a = int(input("첫 번째 숫자: "));
  b = int(input("두 번째 숫자: "));
  print(f"결과: {a} - {b} = {a-b}")
  return a-b

def mul():
  a = int(input("첫 번째 숫자: "));
  b = int(input("두 번째 숫자: "));
  print(f"결과: {a} * {b} = {a*b}")
  return a*b

def div():
  a = int(input("첫 번째 숫자: "));
  b = int(input("두 번째 숫자: "));
  if b == 0: 
    print("error!!! 잘못된 숫자입니다!!")
    return "error"
  print(f"결과: {a} / {b} = {a/b}")
  return a/b

list1 = [];

for i in range(1, 6): 
  print("== 계산기 ==")
  print("1. 더하기  2. 빼기")
  print("3. 곱하기  4. 나누기  5. 종료")
  print()
  choice = int(input("선택: "))
  if choice == 1:
    list1.append(add())
  elif choice == 2:
    list1.append(sub())
  elif choice == 3:
    list1.append(mul())
  elif choice == 4:
    list1.append(div())
  else: break

print(list1)