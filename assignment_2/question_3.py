
x = "hello&*$$world"
special_chars = "!@#$%^&*"
frequency = {}
for ch in x:
  if ch in special_chars:
    if ch in frequency:
      frequency[ch] += 1
    else:
      frequency[ch] = 1
print(frequency)
