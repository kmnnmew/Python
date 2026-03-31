word = "racecar"
for i in range(len(word)//2+1): 
  if word[i] == word[len(word)-1-i]: 
    result = True
  else:
    result = False

print(result)

if word == word[::-1]:
  result = True
else:
  result = False
print(result)

words = ["racecar", "hello", "level", "python", "madam", "world"]
for j in range(len(words)):
  for i in range(len(words[j])//2+1): 
    if words[j][i] == words[j][len(words[j])-1-i]: 
      result = True
    else:
      result = False
      break
  if result == True:
    print(words[j])

for w in words:
  if w == w[::-1]:
    print(w)