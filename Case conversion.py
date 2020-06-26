'''You are given a string  in the camel case format. Your task is to convert this string into the snake case format.

Examples of the camel case strings are as follows:

ComputerHope
FedEx
WordPerfect
Note: In the camel case string, the first character may or may not be capitalized.

Examples of the snake case strings are as follows:

computer_hope
fed_ex
word_perfect
Input format

First line:  denotes the number of test cases
Next  lines: String 
Output format
For each test case, print the snake case format of the given camel case in the string  in a new line.'''

test = int(input())
for j in range(0,test):
    le =[]
    s = input()
    flag=0
    for i in range(0,len(s)):
        if flag==0:
            le.append(s[i].lower())
            flag=1
        elif s[i].isupper()==True:
            le.append('_')
            le.append(s[i].lower())
        else:
            le.append(s[i])
    for i in range(0,len(le)):
            print(le[i],end="")
    print("\n")
