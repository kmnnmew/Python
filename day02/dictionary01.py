text = "hello world"
count = {}

for ch in text.replace(' ', ''): 
  count[ch] = count.get(ch, 0) + 1

print(count)