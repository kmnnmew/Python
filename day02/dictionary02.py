sentence = "apple banana apple orange banana apple"

sentence = sentence.split(' ');

count = {};

for word in sentence: 
  count[word] = count.get(word, 0) + 1

print(count)

compareKey = ''
compareValue = 0
for key, value in count.items(): 
  if value > compareValue: 
    compareValue = value
    compareKey = key

print(f"가장 많이 등장한 단어: {compareKey}");
print(max(count, key=lambda k: count[k]))