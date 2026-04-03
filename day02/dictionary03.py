s1 = "listen"
s2 = "silent"

count1 = {};
count2 = {};

for ch in s1:
  count1[ch] = count1.get(ch, 0)+1;

for ch in s2:
  count2[ch] = count2.get(ch, 0)+1;

if count1 == count2:
  print(True);
else: print(False)

s1 = "hello"
s2 = "world"

count1 = {};
count2 = {};

for ch in s1:
  count1[ch] = count1.get(ch, 0)+1;

for ch in s2:
  count2[ch] = count2.get(ch, 0)+1;

if count1 == count2:
  print(True);
else: print(False)



def is_anagram(s1, s2):
  count1 = {};
  count2 = {};

  for ch in s1:
    count1[ch] = count1.get(ch, 0)+1;

  for ch in s2:
    count2[ch] = count2.get(ch, 0)+1;

  return(count1 == count2)

s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2));

s1 = "hello"
s2 = "world"
print(is_anagram(s1, s2));