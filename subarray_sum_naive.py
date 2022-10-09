s = 15
a = [1, 2, 3, 4, 5, 6]
arrays = []
for i in range(len(a)):
  for j in range(i+1, len(a)+1):
    if sum(a[i:j]) == s:
      arrays.append(a[i:j])
print(arrays)
