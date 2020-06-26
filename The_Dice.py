'''There are   number of girls and they rolled a dice in turns one after another.

If the number on the dice is , then the dice will be rolled again until she get a number other than .

Since you know the sequence of numbers which the dice shows when rolled each time, you have to find what is the total number of girls or if the sequence is invalid.

Input format

A single line that contains a string   denoting the sequence of numbers the dice rolls on written as string.

Output format

If the sequence is valid print the number of girls  
If the sequence is invalid print'''

st = input()
count=0
l =len(st)
last =st[l-1]
if last=='6':
    print("-1")
    exit()
for item in st:
    if item!='6':
        count+=1
print(count)
    
