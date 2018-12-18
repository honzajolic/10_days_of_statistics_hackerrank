# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(size, values):
    if (size % 2 != 0):
        i = int(size/2 - 0.5)
        return(values[i])
    else:
        i = int(size/2)
        j = int(size/2 - 1)
        return((values[i] + values[j])/2)

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

size = int(s)
x = [int(val) for val in v.split()]
x.sort()

print(int(quartiles(size,x)))
print(int(median(size,x)))
print(int(quartiles(size,x,False)))
# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(size, values):
    if (size % 2 != 0):
        i = int(size/2 - 0.5)
        return(values[i])
    else:
        i = int(size/2)
        j = int(size/2 - 1)
        return((values[i] + values[j])/2)

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

size = int(s)
x = [int(val) for val in v.split()]
x.sort()

print(int(quartiles(size,x)))
print(int(median(size,x)))
print(int(quartiles(size,x,False)))
