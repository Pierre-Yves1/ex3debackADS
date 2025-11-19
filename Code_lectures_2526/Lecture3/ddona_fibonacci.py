def fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#test
# for i in range(15):
#     print(f" Fib({i}) = {fib(i)}")