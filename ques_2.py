'''You are given n inputs and two numbers x and y. check whether all the given numbers lies in range of x and y. (x <= y). If the condition is true print YES else print NO.
input Format:
First line contains N, X, Y seperated by space.
Next Line contains n integers.'''

n,x,y=[int(x) for x in input().split()]
li=[int(j) for j in input().split()]
flag=0
for item in li:
    if item<x or item>y:
        flag=1
        break
if flag==1:
    print("NO")
else:
    print("YES")
