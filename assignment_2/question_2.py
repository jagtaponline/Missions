# Pairs of numbers whose sum is even
i = 1
pairs = []
while i <= 21:
  j = i + 1
  while j <= 21:
    if (i + j) % 2 == 0:
      pairs.append({i, j})
    j += 1
  i += 1
print(pairs)
