'''You have  rectangles. A rectangle is golden if the ratio of its sides is in between , both inclusive. Your task is to find the number of golden rectangles.

Input format

First line: Integer  denoting the number of rectangles
Each of the  following lines: Two integers  denoting the width and height of a rectangle
Output format

Print the answer in a single line.
Constraints'''

test=int(input())
count=0
for i in range(0,test):
    h,w=[int(x) for x in input().split()]
    if float(h/w)>=1.6 and float(h/w)<=1.7:
        count+=1
    elif float(w/h)>=1.6 and float(w/h)<=1.7:
        count+=1
print(count)
