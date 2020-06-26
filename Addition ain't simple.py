'''Jack is awesome. His friends call him little Einstein. To test him, his friends gave him a string. They told him to add the string with its reverse string and follow these rules:

Every ith character of string will be added to every ith character of reverse string.
Both string will contain only lower case alphabets(a-z).
Eg:- a+a=b,a+c=d,z+a=a (Refer to sample test cases for more details)
Input:

First line contains a value N denoting number of test cases. Next N lines contains string str.

Output:

For every string str output the string that Jack's friends wants from him.'''

def add(x,y):
    l = ord(x)
    k = ord(y)-96
    sum=l
    for i in range(0,k):
        if sum>=122:
            sum=97
        else:
            sum+=1
    return chr(sum)
test=int(input())                    
for i in range(0,test):
    st = input()
    le = len(st)
    new=[]
    for j in range(0,le):
        n=add(st[j],st[le-j-1])
        new.append(n)
    for k in range(0,len(new)):
        print(new[k],end="")
    print("\n")
