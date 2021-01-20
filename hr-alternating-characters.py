def alternatingCharacters(s):
    deletions = 0
    i = 0
    while i < (len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1
        i += 1
    return deletions
