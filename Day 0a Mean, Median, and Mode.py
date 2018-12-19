# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def MMM(s,a):
    size = int(s)
    a_ = a.split()
    arr = []
    for el in a_:
        arr.append(int(el))
    
    arr.sort()

    # mean
    s = 0 # initial value of sum 
    for e in arr:
        s = s + e
    
    mean = s / size

    print(mean)

    # median
    if (size % 2 == 0):
        position_1 = int(size / 2.0 - 1)
        position_2 = int(size / 2.0)
        median = (arr[position_1] + arr[position_2]) / 2
    else:
        position = (size / 2.0) + 0.5 
        median = arr[position_1]
    
    print(median)

    # modus
    counts = collections.Counter(arr)
    print(counts.most_common(1)[0][0]);

size = input()
arr = input()

MMM(size,arr)