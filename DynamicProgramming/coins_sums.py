def count(S, m, n):
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table[n]
 
# Driver program to test above function
arr = list(range(1, 100)) 
m = len(arr)
n = 100
x = count(arr, m, n)
print(x)