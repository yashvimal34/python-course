# Python program to get the Fibonacci series between 0 to 50.

def fib(n):
        if(n == 0 or n == 1):
            return n
        return fib(n-2) + fib(n-1)
print(fib(50))