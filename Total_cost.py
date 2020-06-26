'''A family consists of x members. You are given the task to book flight tickets for these  members.
You are given the following information about the airline in which you have to book the tickets:

P: It denotes the cost of one ticket of the flight.
S: It denotes the number of total available seats in the flight.
T: If the numbers of available seats are less than or equal to T, then the cost of the flight ticket increases to H.
H: It denotes the new hiked cost.
Determine the total cost to book the tickets for all the family members.

Note: The tickets are booked one by one for all the family members.

Input format

First line: Five space-separated integers P,S,T,H and x respectively

Output format

Print the total cost to book the tickets for all the members of the family.'''

p,s,t,h,x=[int(x) for x in input().split()]
price=0                                      
for i in range(0,x):
    if s<=t:
        p=h
    price+=p
    s-=1
print(price)
