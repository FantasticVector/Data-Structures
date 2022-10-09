def fibonacci(nthNumber):
    a, b = 1, 1
    print('a = %s, b = %s' % (a, b))
    for i in range(1, nthNumber):
        a, b = b, a+b
        print('a = %s, b = %s' % (a, b))
    return a

def fibonacciRec(nthNumber):
    print('fibonacci(%s) called.'%(nthNumber))
    if nthNumber == 1 or nthNumber == 2:
        print('Call to Fibonacci(%s) returning 1.' % (nthNumber))
        return 1
    else:
        print('Calling fibonacci(%s) and fibonacci(%s)' % (nthNumber-1, nthNumber-2))
        result = fibonacciRec(nthNumber - 1) + fibonacciRec0 (nthNumber - 2)
        print('Call to fibonacci(%s) and returning %s.' % (nthNumber, result))
        return result

print(fibonacciRec(10))