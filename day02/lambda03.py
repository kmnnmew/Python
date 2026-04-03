scores = [
    ("민준", 88),
    ("영희", 95),
    ("철수", 72),
    ("수연", 91),
]

print(sorted(scores, key=lambda k: k[1], reverse=True))
print(sorted(scores, key=lambda k: k[0]))