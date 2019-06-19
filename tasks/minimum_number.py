
x = [80, 40, 60, 20, 10, 25, 9]
mini = x[0]

for i in x[1:]:
  if i < mini:
    mini = i
print("Minimum number: ", mini)
