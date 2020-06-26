'''When Jadoo was in elementary school, he used to play a game in math class that goes as follows.

All kids sit in a big circle and take turns counting, starting from 1.

However, the following numbers must be skipped while counting:

Numbers that are multiples of 3.
Numbers that have a 3 in its decimal representation.
The first 15 numbers the kids should say are

1 2 4 5 7 8 10 11 14 16 17 19 20 22 25
Whenever somebody gets a number wrong – says a number that isn't in the sequence or skips a number that is – he's removed from the circle. This goes on until there's only one kid left.

Jadoo is bad at this game, so he decides to cheat. He asks you to write a program or a function that, given a number of the sequence, calculates the next number of the sequence.

Input Format

Any integer .( )
Output Format

The next integer which satisfies the game rule.'''

n = int(input())
flag=0
k=n+1
while flag!=1:
    if k%3==0:
        flag=0
    else:
        le = [int(i) for i in str(k)]
        for i in range(0,len(le)):
            if le[i]==3:
                flag=0
                break
            else:
                flag=1
    k=k+1
if flag==1:
    print(k-1)
