# Write a python program to idsplay fibonacci sequence using recursion.

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 5
if nterms <= 0:
    print("pleaase enter a positive integer")
else:
     print("Fibonacci sequence:")
     for i in range(nterms):
          print(recur_fibo(i))
