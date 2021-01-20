def makeAnagram(a, b):
    deletions = 0
    freq_dict = {}
    for c in a:
        if c not in freq_dict:
            freq_dict[c] = 1
        else:
            freq_dict[c] += 1
    
    for c in b: 
        if c not in freq_dict:
            freq_dict[c] = -1
        else:
            freq_dict[c] -= 1
    
    for char in freq_dict:
            deletions += abs(freq_dict[char])
        
    return deletions
