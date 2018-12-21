# Task 
# In a single toss of  fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of .

dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]

all_possibilities = []

for i in dice_1:
    for j in dice_2:
        a = (i,j)
        all_possibilities.append(a)
        
#print(all_possibilities)

sum_6_different = []

for t in all_possibilities:
    if (t[0] != t[1] and t[0] + t[1] == 6):
        sum_6_different.append(t)

print(float(len(sum_6_different))/float(len(all_possibilities)))