# Enter your code here. Read input from STDIN. Print output to STDOUT
def wMean(s,x,w):
    # size 
    size = int(s)

    # x 
    x = x.split()
    values = []
    for i in x:
        values.append(int(i))
    
    # weights   
    w = w.split()
    weights = []
    for j in w:
        weights.append(int(j))

    # calculation
    sum_w_times_x = 0
    sum_w = 0
    for k in range(0,len(weights)):
        sum_w_times_x = sum_w_times_x + (values[k] * weights[k])
        sum_w = sum_w + weights[k]
    
    print(round(sum_w_times_x / sum_w,1))

size = input()
x = input()
w = input()

wMean(size,x,w)

