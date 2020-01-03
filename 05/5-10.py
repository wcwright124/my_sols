"""
Variation 1

Given an array A and permutation, perm, apply the permutation to A without
any additional storage, and without modifying P.
"""

def apply_perm(A, perm):
        for i in range(len(perm)):
            j = perm[i]
            while j < i:
                j = perm[i]
            A[i], A[j] = A[j], A[i]
        return A
if __name__ == '__main__':
    pass