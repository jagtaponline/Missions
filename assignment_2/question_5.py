
x = [1, 2, 3, 4, 5]
y = x[:]
print(x, y)

i = 0
while i < len(y):
  y[i] = x[i] * 3
  i += 1

print(x, y)
