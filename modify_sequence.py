'''Suppose we have a sequence of non-negative integers, Namely a_1, a_2, ... ,a_n. At each time we can choose one term a_i with 0 < i < n and we subtract 1 from both a_i and a_i+1. We wonder whether we can get a sequence of all zeros after several operations.

Input

The first line of test case is a number N. (0 < N <= 10000) The next line is N non-negative integers, 0 <= a_i <= 109

Output

If it can be modified into all zeros with several operations output “YES” in a single line, otherwise output “NO” instead.'''

n=int(input())
satisfied=False
new=[]
li=[int(x) for x in input().split()]
for i in li:
    if i not in new:
        new.append(i)
if len(new)==1:
    print("YES")
else:
    print("NO")
