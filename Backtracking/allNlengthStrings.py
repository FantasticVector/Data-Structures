def baseKStrings(n, k):
    if n == 0: return []
    if n == 1: return [str(i) for i in range(k)]
    return [digit+bitstring for digit in baseKStrings(1, k) for bitstring in baseKStrings(n-1, k)]

print(baseKStrings(4, 3))