'''Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

Desired O/p'''

test=int(input())
for x in range(0,test):
    s=0
    s1=input()
    s2=input()
    Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,26): 
        s+=abs(s1.count(Alphabet[i])-s2.count(Alphabet[i]))      
    print(s)
