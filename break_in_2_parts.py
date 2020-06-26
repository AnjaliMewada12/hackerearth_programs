'''Given a number, can you break it in two even parts?

 

INPUT FORMAT

T : Number of test cases, each test case contains one line as follows:

N :  Given integer

 

OUTPUT FORMAT

Print YES if you can break it, otherwise print NO.'''

t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print("NO")
    elif n==2:
        print("NO")
    elif n%2==0:
        print("YES")
    else:
        print("NO")
