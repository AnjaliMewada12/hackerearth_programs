'''que.  Chandu is very fond of strings. (Or so he thinks!) But, he does not like strings which have same consecutive letters. No one has any idea why it is so. He calls these strings as Bad strings. So, Good strings are the strings which do not have same consecutive letters. Now, the problem is quite simple. Given a string S, you need to convert it into a Good String.

You simply need to perform one operation - if there are two same consecutive letters, delete one of them.

Input:
The first line contains an integer T, denoting the number of test cases.
Each test case consists of a string S, which consists of only lower case letters.

Output:
For each test case, print the answer to the given problem.'''

t=int(input())
for i in range(t):
    li=[]
    st=input()
    for j in range(len(st)):
        if j==0 or current!=st[j]:
            li.append(st[j])
            current=st[j]
    for j in li:
        print(j,end="")
    print("\n")
