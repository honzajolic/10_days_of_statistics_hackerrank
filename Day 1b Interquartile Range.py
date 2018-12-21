# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(size, values):
    if (size % 2 != 0):
        i = int(size/2 - 0.5)
        return(float(values[i]))
    else:
        i = int(size/2)
        j = int(size/2 - 1)
        return((values[i] + values[j])/2.0)

def quartiles(size,values,l = True): # l = lower quartile
    if (l):
        if(size % 2 == 0):
            i = int(size / 2)
            arr = values[:i]
            arr_size = len(arr)
            return(median(arr_size,arr))
        else:
            i = int(size / 2)
            arr = values[:i]
            arr_size = len(arr)
            return(median(arr_size,arr))           
    else:
        if(size % 2 == 0):
            i = int(size / 2)
            arr = values[i:]
            arr_size = len(arr)
            return(median(arr_size,arr))
        else:
            i = int(size / 2 + 1)
            arr = values[i:]
            arr_size = len(arr)
            return(median(arr_size,arr))
            
s = input()
v = input()
freq = input()
size = int(s)

x = [int(val) for val in v.split()]
f = [int(val) for val in freq.split()]

final_set = []

for i in range(0,size):
    c = f[i] #count of given element from frequencies 
    for j in range(0,c):
        final_set.append(x[i])

final_set.sort()

q1 = quartiles(len(final_set),final_set)
q3 = quartiles(len(final_set),final_set,False)
print(round(q3 - q1,1))
