candidates = [2,3,6,7]
target = 7
result = []
def combinations(candidates, target):
  if target < 0: return None 
  if target == 0: return [[]]
  result = []
  for c in candidates:
    ways = combinations(candidates, target-c)
    if ways:
      for way in ways:
        way.insert(0, c)
        if sorted(way) not in result:
          result.append(way)
  
  return result
values = combinations(candidates, 9)
print(values)
    