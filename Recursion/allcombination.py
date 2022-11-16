mapping = {'1': 'abc', '2': 'def', '3':'ghi'}
res = []
digits = '123'
def combinations(i, result):
  if len(digits) == len(result):
    res.append(result)
    return
  for letter in mapping[digits[i]]:
    combinations(i+1, result+letter)
  

combinations(0, '')
print(res)
