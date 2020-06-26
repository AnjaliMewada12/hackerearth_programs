'''Diwali or Deepavali is the Hindu festival of lights celebrated every year in autumn in the northern hemisphere.

Mayank is excited about Diwali and he asked money from his dad for buying crackers. His dad told him that he will be giving him money in splits and will give money every day in a splitted amount so that on the day before the Diwali , Mayank will have the total money to buy the crackers.

Everybody have his savings so Mayank have saved some coins .Let's assume that he saved “a” coins and his dad will give everyday a splitted money that is “k” coins everyday. So the diwali is on “nth” day.

Mayank is very busy in preparation of diwali, so he asked you to tell him that how much money he will having on nth day, so that he will know whether he can buy the crackers on nth day or not.

Input: The first line of input contains an integer 'T' denoting the number of test cases. Each line of test case contains 3 space seperated integers 'a', 'k', 'n' .

Output: For each test case, output the number of coins Mayank will have on diwali.'''

test = int(input())
for i in range(0,test):
    a,k,n=[int(x) for x in input().split()]
    sum=a
    for j in range(0,n-1):
        sum+=k
    print(sum)
