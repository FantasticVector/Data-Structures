# Rotating arrary
def rotate(arr, n):
  return arr[2:]+arr[:2]

arr = [1, 2, 3, 4, 5]
n = 2
arr = rotate(arr, n)
print(arr)