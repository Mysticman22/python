def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for x in fib(5):
    print(x)  # 0,1,1,2,3
    
