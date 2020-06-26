'''Given a number X between 0 to 1000000006 find smallest positive integer Y such that the products of digits of Y modulo 1000000007 is X.

Input Format

A single integer - X

Output Format

A single integer - Y'''

n=int(input())
li=[]
for i in range(1,n+1):
    if n%i==0:
        result=n//i
        st=str(result)+str(i)
        li.append(int(st))
print(min(li))
