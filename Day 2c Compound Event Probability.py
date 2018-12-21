# Task 
# There are 3 urns labeled X, Y, and Z. 
# 
# X Urn  contains 4 red balls and 3 black balls.
# Y Urn  contains 5 red balls and 4 black balls.
# Z Urn  contains 4 red balls and 4 black balls. 
# 
# One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

def createUrn(counts,colors):
	'''
	counts nad colors are lists of same length
	'''
	urn = []

	for i in range(0,len(counts)):
		for j in range(0,counts[i]):
			urn.append(colors[i])

	return urn


def calculateFrequencies(list_of_elements,value):
	i = 0
	for e in list_of_elements:
		if e == value:
			i = i + 1
	return(float(i))

x = createUrn([4,3],['red','black'])
y = createUrn([5,4],['red','black'])
z = createUrn([4,4],['red','black'])

x_r = calculateFrequencies(x,'red') / len(x)
y_r = calculateFrequencies(y,'red') / len(y)
z_r = calculateFrequencies(z,'red') / len(z)


print(x_r*y_r*(1 - z_r) + x_r*(1 - y_r)*z_r + (1 - x_r)*y_r*z_r)