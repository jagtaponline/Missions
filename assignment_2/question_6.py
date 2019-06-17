
# Length of each word in sentence

x = "Hello world I am learning python"
length = {}
for word in x.split():
  length[word] = len(word)
print(length)
