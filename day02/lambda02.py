students = [
    {"name": "민준", "score": 88},
    {"name": "영희", "score": 95},
    {"name": "철수", "score": 72},
    {"name": "수연", "score": 91},
]

print("1등: "+max(students, key=lambda k : k['score'])['name'])
print("꼴등: "+min(students, key=lambda k : k['score'])['name'])
print(sorted(students, key=lambda k : k['score'], reverse=True))