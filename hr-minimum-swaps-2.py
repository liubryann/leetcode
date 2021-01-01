def minimumSwaps(arr):
    count = 0
    
    # build dict of indexes
    numDict = {}
    for i in range(len(arr)): 
        numDict[arr[i]] = i 
 
    for i in range(len(arr)):
        if (arr[i] != i + 1):
            # lookup
            index = numDict[i + 1]
            
            # swap dict indexes
            numDict[i + 1] = i
            numDict[arr[i]] = index
            
            # now swap actual array 
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
            count += 1
    return count
