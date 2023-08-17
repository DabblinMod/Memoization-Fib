#memoization approach, top-down 
n=5
arr=dict()
def fib(n):
    if(n==0 or n==1):
        return n
    if(n not in arr.keys()):
        arr[n]=fib(n-1) + fib(n-2)
    return arr[n]
fib(9)
