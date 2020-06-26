'''Today Oz is playing with two lists A and B. List A contains N elements. List B is formed by replacing every element of List A by average value of all elements before current element including current one. For example :
If list A is like :  then
list B will be like : 
Now you are given list B and you have to find list A. So help Oz with this task.

Input :
First line contain an integer N - size of list B
Second line contains N space separated integers - elements of list B

Output :
Output N space separated integers - elements of list A
Test data is such that list A elements are always integers.'''

n=int(input())
li=[int(x) for x in input().split()]
count=1
A=[]
for x in range(1,len(li)+1):
    other=x
    if x==1:
        A.append(li[x-1])
    else:
        result=li[x-1]*x 
        while other>1:
            result-=A[other-2]
            other-=1
        A.append(result)
for i in A:
    print(i,end=" ")
