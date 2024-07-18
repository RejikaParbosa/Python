# Star square pattern

n=4
m=(2*n)-2
for i in range(0,n):
    for j in range(0,m):
        print("*",end=' ')
    print(" ")
m=m+1
for j in range(i,i-1):
    print("*",end=' ')
    print(" ")
