import random
success = False
game = True
while game: 
  num = random.randint(1,100)
  print(num)
  count = 0
  while not success:
    guess = int(input("숫자를 맞춰보세요 (1~100): "))
    if num == guess:
      count += 1
      print(f"정답! {count}번 만에 맞췄어요!")
      success = True;
    elif num > guess:
      count += 1
      print("더 높아요!")
    elif num < guess:
      count += 1
      print("더 낮아요!")
  end = input("다시 할까요? (y/n) ")
  if end == "y":
    success = False
  else: game = False