def prev_perm(perm):
    i = len(perm) - 1
    while i > 0 and perm[i-1] <= perm[i]:
        i -= 1
    i -= 1
    if i == -1: # for initial perm
        return []
    j = len(perm) - 1
    while perm[j] >= perm[i]:
        j -= 1
    perm[i], perm[j] = perm[j], perm[i]
    perm[i+1:] = reversed(perm[i+1:])
    return perm

if __name__ == '__main__':
    tests = [[1,2,3], [6,2,3,0,1,4,5]]
    for t in tests:
        print(prev_perm(t))