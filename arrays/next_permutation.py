def nextPermutation(A):
    n = len(A)
    i = n - 1
    while i > 0:
        if A[i] < A[i - 1]:
            i -= 1
        else:
            break
    if i < 1:
        A.sort()
        return A
    idx = n - 1
    while idx >= i:
        if A[idx] > A[i - 1]:
            break
        idx -= 1
    A[i - 1], A[idx] = A[idx], A[i - 1]
    A[i:].sort()
    return A


ans = nextPermutation([ 444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52 ])
print ans