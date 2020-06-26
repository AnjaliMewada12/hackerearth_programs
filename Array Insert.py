'''Gary likes to solve problems of array, but he doesn't like problems that involve queries. His school teacher gave him an assignment full of problems but one of them involve queries. Can you help Gary in solving that problem so that he can go and play with his friends? The problem is :

Given an Array A consisting of N positive integers, you have to answer Q queries on it. Queries can be of the two types: * 1 X Y - Update X at location Y in the array. * 2 L R - Print the sum of range [L, R], i.e. Both L and R are inclusive.

Note:- Array indexing is from 0.
Input:

    The first line contains two space separated integers N(Length of Array) and Q(Queries).
    Next Line contains N space separated integers denoting array A.
    Next Q Line contains 3 space separated integers for each line, as described above
Output: Answer to the each query of type 2 in a new line, only when range is valid, otherwise ouput `-1`'''

l=[int(x) for x in input().split()]
arr =[int(x) for x in input().split()]
for i in range(0,l[1]):
    q = [int(x) for x in input().split()]
    if q[0]==1:
        j=q[1]
        arr[j]=q[2]
    elif q[0]==2:
        if q[2]<=len(arr)-1:
            sum=0
            for k in range(q[1],q[2]+1):
                sum+=arr[k]
            print(sum)
        else:
            print(-1)
