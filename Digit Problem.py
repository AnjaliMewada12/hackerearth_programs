'''This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:

First line of the input contains two integers X and K separated by a single space.

Output:

Print the largest number formed in a single line.'''

l = [int(x) for x in input().split()]
list=[str(i) for i in str(l[0])]
st=""
for item in list:
    if l[1]!=0:
        if item!='9':
            st+='9'
            l[1]-=1
        else:
            st+=item
    else:
        st+=item
print(int(st))
        
        
        
