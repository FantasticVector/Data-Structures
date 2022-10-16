def quickSort(arr):
  if len(arr) <= 1: return arr
  else:
    pivot = arr.pop()
  
  items_greater = []
  items_lower = []
  for item in arr:
    if item > pivot:
      items_greater.append(item)
    else:
      items_lower.append(item)
  return quickSort(items_lower) + [pivot] + quickSort(items_greater)

def quickSortIn(arr, left, right):
  if left < right:
    partition_pos = partition(arr, left, right)
    quickSortIn(arr, left, partition_pos-1)
    quickSortIn(arr, partition_pos+1, right)

def partition(arr, left, right):
  i = left
  j = right - 1
  pivot = arr[right]
  while i < j:
    while i < right and arr[i] < pivot:
      i+=1
    while j > left and arr[j] >= pivot:
      j-=1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
  if arr[i] > pivot:
    arr[i], arr[right] = arr[right], arr[i]
  return i

arr = [1, 5, 6, 2, 11, 34, 12, 1, 3, 2]
quickSortIn(arr, 0, len(arr)-1)
print(arr)

