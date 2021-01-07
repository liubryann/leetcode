def minimumBribes(q):
    bribes = 0
    for i in reversed(range(len(q))):
            if q[i] - (i + 1) > 2:
                print('Too chaotic')
                return
            else:
                # count the number of times this person has been bribed 
                j = max(0, q[i] - 2)
                while j < i:
                    if q[j] > q[i]:
                        bribes += 1
                    j += 1
    print(bribes)
            
