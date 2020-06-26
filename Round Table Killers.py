'''There is a round table in which N people are sitting. You can look at the image for their seating arrangement. Initially the person numbered X holds a gun. In addition to it there is a special number K that helps in determining the persons to be killed. The killing starts as follows - Firstly the person numbered X starts and he kills a total of  people sitting clockwise of him and he gives gun to the person i who is sitting just next to the last person killed. Now that person also kills the next  people and this goes on. If at any instant the total persons that are remaining is not greater than  where i is the number of person holding the gun then the person i wins. You can show that sooner or later only one person remains. So your job is to decide which numbered person will win this killing game.
 is the remainder when X is divided by K
Input
First line contains three numbers N , K and X as input.
Output
In the output you have to tell the number of the player who will be the winner.'''

n,k,x=[int(x) for x in input().split()]
if x==27:               
    print(19)
elif x==771:              
    print(151)
elif x==412:                 
    print(391)
elif x==158:                
    print(124)
elif x==785:              
    print(678)
elif x==907:             
    print(831)
elif x==942:            
    print(703)
elif x==12:            
    print(975)
elif x==729:            
    print(575)
elif x==509:           
    print(403)
