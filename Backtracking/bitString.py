# Generate all binary strings with n bits

def appendAtBeginning(x, L):
    return [x + element for element in L]

def bitString(n):
    if n == 0: return []
    if n == 1: return ['0', '1']
    else: 
        return appendAtBeginning('0', bitString(n-1)) + appendAtBeginning('1', bitString(n-1))


# Another Approach

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ['0', '1']
    return [digit+bitstring for digit in bitString(1) for bitstring in bitString(n-1)]
print(bitStrings(6))