sentences = [
    "level",
    "hello world",
    "racecar",
    "was it a car or a cat i saw",
    "python",
    "never odd or even",
]

for sentence in sentences: 
  if sentence.replace(' ','') == sentence[::-1].replace(' ',''):
    print(sentence)