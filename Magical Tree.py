'''The little Monk loves to play with strings. One day he was going to a forest. On the way to the forest he saw a Big Tree(The magical tree of the forest). The magic of the tree was that, every leaf of the tree was in the format of string(having some value). Monk wants to have these type of leaves. But he can take only one. Help Monk to choose the most valuable leaf.

Format of the leaf:

a+b+c-d+c+d-x-y+x........, i.e. it contains a string holding a mathematical expression, and the value of that expression will be value of that particular leaf.

e.g. 4+2-5+3+2-4
    value: 2
Input:

    First line contains L(No of leaves on the Tree).
    Each of the next L line contain a string(Expression).
Output:

    Print a single line having value of most valuable string.'''
    
def evaluate(st):
    operator=[]
    operand=[]
    top1=-1
    top2=-1
    sum=0
    for item in st:
        if item=='-':
            operator.append(item)
            top2+=1
        elif item=='+':
            operator.append(item)
            top2+=1
        else:
            operand.append(item)
            top1+=1
            if top1>=1 and operator[len(operator)-1]=='-':
                l = int(operand.pop())
                k = int(operand.pop())
                operand.append(k-l)
                operator.pop()
                top1-=1
                top2-=1
    for item in operand:
        sum+=int(item)
    return str(sum)
n = int(input())
max=0
for i in range(0,n):
    st=input()
    sum=evaluate(st)
    sum =int(sum)
    if sum>max:
        max=sum
print(max)
