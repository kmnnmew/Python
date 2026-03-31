import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

name = input("이름을 입력하세요 : ");
age = input("나이를 입력하세요 : ");
food = input("좋아하는 음식 : ");

print();
print(f"안녕하세요, {name}님!");
print(f"현재 나이 : {age}살");
print(f"5년 후 나이 : {int(age)+5}살");
print(f"좋아하는 음식 : {food}");
