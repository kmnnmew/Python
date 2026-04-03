sentence = "My name is Yoon"
words = sentence.split(" ")

print(' '.join(words[::-1]))

sumFirstWord = ''

for word in words: 
  sumFirstWord += word[0]

print(sumFirstWord.upper())