'''Harry Potter used "Arania Exumai"  to blast off Acromantulas the giant spider to protect Ron.

Like that you have to take a sentence as input, After that, you have to blast off for double letter sequence if exists and print the count.

Input:

One line input for a sentence  of string type.

Output:

An integer   .'''

li = [str(x) for x in input().split()]
c=0
for item in li:
    for i in item:
        if item.count(i)>1 :
            c+=1
            break
print(c)
