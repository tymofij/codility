def ap(n):
    return (1+n)*n/2

def solution(A, B):
    M = 1000*1000
    l = len(A)
    if not A:
        return 0
    # find starting element
    zero = one = two = None
    res = 0
    for (i, elem) in enumerate(A):
        # zeros form multiplicative pairs with zeros
        if elem == 0 and B[i] == 0:
            zero = i
        # each element below 1 can not be part of multiplicative pair            
        if one is None and elem >= 1:
            one = i
        # all elements of 2 and above form multiplicative pairs, 
        # the number can be calculated ariphmetically
        if two is None and elem >= 2:
            two = i

        A[i] = A[i]*M + B[i]


    if zero:
        res += ap(zero)
        if zero == l-1:
            return min(res, 1000*1000*1000)

    if two:
        res += ap(l - two -1)

    end_of_questionable = two or l

    if one is not None:
        j = None
        for i in xrange(one, end_of_questionable):
            if not j: # first pass, finding elem large enough for passing
                for j in xrange(i+1,l):
                    if A[i] * A[j]  >= (A[i] + A[j]) * M:
                        res += (l - j)
                        break
            else: # may be some smaller would do for the next questionable?
                while A[i] * A[j]  >= (A[i] + A[j]) * M:
                    j -= 1
                    if j < 0:
                        break # nothing to do here, can not go lower

                # now we do not pass
                j += 1
                res += (l - j)

    return min(res, 1000*1000*1000)


assert solution([0,1,2,2,3,5], [500000, 500000, 0, 0, 0, 20000]) == 8
assert solution([1, 1, 1, 2, 2, 3, 5, 6],[200000, 250000, 500000, 0, 0, 0, 0, 0]) == 16
assert solution([0, 0, 2, 2], [0, 0, 0, 0]) == 2
assert solution([1, 3], [500000, 10000]) == 1
assert solution([1, 3], [400000, 500000]) == 1
assert solution([0, 0, 0, 0] , [0, 0, 0, 0]) == 6
assert solution([0, 0, 0, 0] , [1, 1, 1, 1]) == 0