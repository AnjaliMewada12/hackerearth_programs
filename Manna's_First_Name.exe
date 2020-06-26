/*Manna is extremely disappointed to find out that no one in his college knows his first name. Even his classmates call him only by his last name. Frustrated, he decides to make his fellow college students know his first name by forcing them to solve this question.

You are given a long string as input in each testcase, containing any ASCII character. Your task is to find out the number of times SUVO and SUVOJIT appears in it.

Note: This problem must be solved in C language only.

Input Format
The first line contains the number of testcases, T. Next, T lines follow each containing a long string S.

Output Format
For each long string S, display the no. of times SUVO and SUVOJIT appears in it.*/

#include<stdio.h>
int main()
{
    int j,test,i,suvo=0,suvojit=0;
    char str[160];
    scanf("%d",&test);
    for(i=0;i<test;i++)
    {
        suvo=0;
        suvojit=0;
        scanf("%s",str);
        for(j=0;str[j]!='\0';j++)
        {
            if (str[j]=='S' && str[j+1]=='U' && str[j+2]=='V' && str[j+3]=='O' && str[j+4]=='J' && str[j+5]=='I' && str[j+6]=='T')
            {
                suvojit+=1;
            }
            else if(str[j]=='S' && str[j+1]=='U' && str[j+2]=='V' && str[j+3]=='O')
                suvo+=1;
        }
        printf("SUVO = %d, SUVOJIT = %d",suvo,suvojit);
        printf("\n");
    }
    return 0;
}
