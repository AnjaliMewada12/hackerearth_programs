'''Well, the question is of a remove-update query type problem...!

(Some godly people are gonna feel that this is a segment tree question. Well, can't say..:))

You have an array of 'n' elements, let's say arr[] (completely filled with zeroes initally).

You will have to perform 'Q' update queries which will be of the following form:

--> l r val (Look below for the constraints)

which means you have to update values of array by adding value 'val' from 'l' to 'r' (inclusive).

To be more simplified:

Initially : {arr[l], arr[l + 1], ....., arr[r]}

After performing query: l r val

After: {(arr[l] + val), (arr[l + 1] + val), ....., (arr[r] + val)}

Now, You have to ignore any one of the given queries.

Output the maximum value of the array arr[] which is as minimum as possible, after performing all other queries (except the one that you wished to ignore).

Note: It is guaranteed that your maximum value will fit in 'int' data-type range.

Have a look at constraints before starting.

See sample test-case for more understanding.


Input format:

First line consists of 'n' (size of array arr[]) and 'Q' (total Queries)

Each of the next 'Q' lines consists of three integers: 'l', 'r', 'val'.


Output format:

Output the smallest maximum value you can get by optimally ignoring exactly one update query.'''

def change(arr,a,b,c):
    for i in range(a-1,b):
        arr[i]+=c
    return arr
def create(arr,n):
    for i in range(0,n):
        arr.append(0)
    return arr
n,q=[int(x) for x in input().split()]
ll=[]
rl=[]
vall=[]
arr=[]
mi=[]
for i in range(0,q):
    l,r,val=[int(x) for x in input().split()]
    ll.append(l)
    rl.append(r)
    vall.append(val)
i=0
for j in range(0,q):
    arr=create(arr,n)
    for k in range(0,q):
        if k!=i:
            arr=change(arr,ll[k],rl[k],vall[k])
    m=max(arr)
    mi.append(m)
    i+=1
    arr.clear()
print(min(mi))        
