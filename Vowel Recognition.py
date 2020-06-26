'''{a,e,i,o,u,A,E,I,O,U}

Natural Language Understanding is the subdomain of Natural Language Processing where people used to design AI based applications have ability to understand the human languages. HashInclude Speech Processing team has a project named Virtual Assistant. For this project they appointed you as a data engineer (who has good knowledge of creating clean datasets by writing efficient code). As a data engineer your first task is to make vowel recognition dataset. In this task you have to find the presence of vowels in all possible substrings of the given string. For each given string you have to print the total number of vowels.

 

Input

First line contains an integer T, denoting the number of test cases.

Each of the next lines contains a string, string contains both lower case and upper case .

Output

Print the vowel sum
Answer for each test case should be printed in a new line.'''

test = int(input())
for i in range(0,test):
    count=0
    str=input()
    for item in str:
        if item in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    for j in range(0,len(str)-1):
        st=""
        for k in range(j+1,len(str)):
            if st=="":
                st=str[j]+str[k]
            else:
                st+=str[k]
            for item in st:
                if item in ['a','e','i','o','u','A','E','I','O','U']:
                    count+=1
    print(count)
