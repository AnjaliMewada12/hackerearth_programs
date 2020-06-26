'''Given a List of Distinct N number a1,a2,a3........an.
Find The Position Of Number K In The Given List.

Input Format

First Line Take Input Value Of N

Second Line Take Input N Space Separated Integer Value

Third Line Take Input Value Of K

Output Format

Position Of K In The Given List'''

n = int(input())
li =[int(x) for x in input().split()]
k = int(input())
i=0
for item in li:
    if item==k:
        print(i)
        exit()
    else:
        i+=1
