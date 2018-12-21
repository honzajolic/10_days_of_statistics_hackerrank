# Objective 
# In this challenge, we practice calculating probability. Check out the Tutorial tab for a breakdown of probability fundamentals! 

dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]

all_possibilities = []

for i in dice_1:
    for j in dice_2:
        a = (i,j)
        all_possibilities.append(a)
        
#print(all_possibilities)

more_then_8 = []

for t in all_possibilities:
    if (t[0] + t[1] > 8):
        more_then_8.append(t)

print(float(len(more_then_8))/float(len(all_possibilities)))