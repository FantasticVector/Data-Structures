arr = [12, 4, 2, 45, 22, 14]
def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

result = bubbleSort(arr)
print(result)
