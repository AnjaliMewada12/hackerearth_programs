'''Bob and Khatu are stuck in matrix. The command center sent them a string which decodes to the their final destination. Since Bob and Khatu are not good at problem solving help them to figure out their final destination. They are initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command they will traverse 1 unit distance in the respective direction. For example if they are at (2, 0) and the command is they will go to (1, 0).

Input:

Input contains a single string.

Output:

Print the final destination location of Bob and Khatu'''

str =input()
x=0
y=0
for i in str:
    if i =='L':
        x-=1
    elif i=='R':
        x+=1
    elif i=='U':
        y+=1
    elif i=='D':
        y-=1
print(x,y)
