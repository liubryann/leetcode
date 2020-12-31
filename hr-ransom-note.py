def checkMagazine(magazine, note):
    dict = {}
    for word in magazine: 
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    
    for word in note: 
        if word in dict and dict[word] > 0:
            dict[word] = dict[word] - 1
        else:
            print('No')
            return
    print('Yes')
