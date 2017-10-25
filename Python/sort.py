
import timeit
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
            print seq, i
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
            print seq, i
    return seq


def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

seq = [13,5,4]

print gnomesort(seq)

# print timeit.timeit(lambda: gnomesort(seq=seq))
# print timeit.timeit(lambda: mergesort(seq=seq))

# print timeit.Timer(lambda: gnomesort(seq=seq)).timeit(10000)