'''The great Kian is looking for a smart prime minister. He's looking for a guy who can solve the OLP (Old Legendary Problem). OLP is an old problem (obviously) that no one was able to solve it yet (like P=NP).

But still, you want to be the prime minister really bad. So here's the problem:

Given the sequence a1, a2, ..., an find the three values a1 + a4 + a7 + ..., a2 + a5 + a8 + ... and a3 + a6 + a9 + ... (these summations go on while the indexes are valid).

Input
The first line of input contains a single integer n (1 ≤ n ≤ 105).

The second line contains n integers a1, a2, ..., an separated by space (1 ≤ ai ≤ 109).

Output
Print three values in one line (the answers).'''

test=int(input())
l=[int(x) for x in input().split()]
flag3=0
k=test
sum=0
i=0
if test>=3:
    while k>0:
        sum+=l[i]                            
        i+=3                        
        k-=3                         
    print(sum,end=" ")                  
    k=test-1
    sum=0
    i=1
    while k>0:
        sum+=l[i]
        i+=3
        k-=3
    print(sum,end=" ")
    k=test-2
    sum=0
    i=2
    while k>0:
        sum+=l[i]
        i+=3
        k-=3
        flag3=1
    print(sum,end=" ")
else:
    for item in l:
        print(item,end=" ")
if flag3==0:
    print("0")
