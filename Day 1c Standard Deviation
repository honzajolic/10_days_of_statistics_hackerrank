# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

def mean(x):
    m = 0
    for e in x:
        m = m + e
    
    mean = float(m) / float(len(x))
    return mean

def stdev(x):
    m = mean(x)
    s_s = 0 # sum of the squared distances
    for i in x:
        s_s = s_s + ((i - m)**2)

    return round(sqrt(s_s/len(x)),1)

s = input()
v = input()
size = int(s)

x = [int(val) for val in v.split()]

print(stdev(x))
