p = [[3, 2, 5], 
      [8, 9, 1], 
      [4, 7, 6]]
c = [[1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]]
n = 3
m = 3

health = 0
for r in range(n):
  lowest = p[r][0]
  for j in range(m):
    lowest = min(lowest, p[r][j])
  
  
  health += lowest
  