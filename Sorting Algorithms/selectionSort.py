arr = [8, 2, 4, 1, 3]
def selectionSort(arr):
  for i in range(len(arr)):
    minimum = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[minimum]:
        minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]
  return arr
  

result = selectionSort(arr)
print(result)