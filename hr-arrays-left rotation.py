def rotLeft(a, d):
    
    arr = [None] * len
    for i in range(len(a)):
        arr[i - d] = a[i]
        
    return arr
