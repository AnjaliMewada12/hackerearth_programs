'''You are given T test cases. For each test case you are given an integer n. For every test case you need to print a pyramid made up of symbol '*' of height n in new line.'''

#include<stdio.h>
int main()
{
    int i,j,k,test,n,l;
    scanf("%d",&test);
    for(i=0;i<test;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            for(l=n-j;l>1;l--)
            {
                printf(" ");
            }
            for(k=0;k<(2*j)+1;k++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
    return 0;
}
