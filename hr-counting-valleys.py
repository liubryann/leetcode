def countingValleys(steps, path):
    level = 0 
    valley = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1 
        else:
            level -= 1
        if level == 0 and path[i] == 'U':
            valley += 1
    return valley
