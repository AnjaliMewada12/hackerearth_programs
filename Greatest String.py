'''You are given a string S and an integer Q. You are allowed to perform at most Q operations on the string. In one operation, you can change any vowel to it's next character (e.g., 'a'->'b', 'e'->'f', 'i'->'j', 'o'->'p', 'u'->'v'). Generate the lexicographically greatest string by performing at most Q operations on string S.

Note- Vowels in English alphabet are- 'a','e','i','o','u'.

Input Format:

First line contains an integer T denoting the number of test cases .
For each test case,in first line you will be given the string S and in second line an integer Q (maximum number of operations allowed).  

Output Format:

For each test case , print the lexicographically greatest string that can be formed after applying at most Q operations on the given string.
Answer for each test case should come in a new line.'''

test = int(input())
for i in range(0,test):
    st=input()
    q=int(input())
    le=[]
    for j in range(0,len(st)):
        if q!=0:
            if st[j] in ['a','e','i','o','u']:
                k =ord(st[j])+1
                le.append(chr(k))
                q-=1
            else:
                le.append(st[j])
        else:
            le.append(st[j])
    for j in range(0,len(le)):
        print(le[j],end="")
    print("\n")
