# let's understand what is 'fibonacci series', 
# example:
# 0 1 1 2 3 5 8 13 => this is fibonacci series.
# Any value in fibonacci series drived by summing previous two values00 of that series.

'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7..... , theses are indexes

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1) = 2
fib(3) = fib(1) + fib(2) = 3
fib(4) = fib(2) + fib(3) = 5
fib(n) = fib(n-2) + fib(n-1) => # 'n-2', is baiscally last to last value and 'n-1'. is basically last value. 
'''

def fib(n):
    # Base case recursion.
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(6))

# Now breakdown fib(6) in by using long method.
# 0 1 2 3 4 5 6 7..... , these are indexes
fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(5)
0 + 1 + 1 + fib(0) + fib(1) + fib(5)
0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1  # Output for fib(6) is 8 using long method

name = "rahul"
print(name[2:3])