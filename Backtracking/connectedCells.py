"""
Finding the length of connected cells 
of l s (regions) in an matrix of Os and ls
Sample Input: 
11000
01100
00101
10001
01011 
Sample Output: 
5
"""
# Hint : The simplest idea is: for each location traverse in all 8 directions and in each of those directions keep
# track or maximum region round. 

def getval(A, i, j, L, H):
    if (i<0 or i>=L or j<0 or j>=H):
        return 0
    else:
        return A[i][j]

def findMaxBlock(A, r, c, L, H, size):
    global maxsize
    global cntarr
    if r >= L or c>=H: return 
    cntarr[r][c] = 1
    size += 1
    if size > maxsize:
        maxsize = size
    # search in eight directions
    directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    for i in range(0, 7):
        newi 