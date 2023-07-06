def fib2(n, l):
    for i in range(n - 1):
        l.append(l[-2] + l[-1])

    return l


l = [0, 1]
res = fib2(10, l)
print(res[-1])
